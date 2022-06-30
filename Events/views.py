from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from django.contrib.auth.models import User
# Import User Model from Django
from .Forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponse
import csv
from django.contrib import messages

#Create Admin Approval page

def admin_approval(request):
	#Get Counts
	event_count=Event.objects.all().count()
	venue_count=Venue.objects.all().count()
	user_count=User.objects.all().count()


	event_list = Event.objects.all().order_by('-event_date')

	if request.user.is_superuser:
		if request.method=="POST":
			id_list = request.POST.getlist('boxes')

			#uncheck all events
			event_list.update(approved=False)

			# update the database
			for x in id_list:
				Event.objects.filter(pk=int(x)).update(approved=True)
				messages.success(request, ("Event List Approval has been updated"))
			return redirect('list-events')
		else:
			return render(request, 'events/admin_approval.html',
			{"event_list": event_list, "event_count":event_count, "venue_count": venue_count,
			 "user_count": user_count })

	else:
		messages.success(request, ("You are not authorized to approve/view this page"))
		return redirect('home')

	return render(request, 'events/admin_approval.html')

#import pagination stuff
from django.core.paginator import Paginator

#Create My Events page
def My_Events(request):
	if request.user.is_authenticated:
		me = request.user.id
		events = Event.objects.filter(attendees=me)
		return render(request,'events/My_Events.html',
			{'me': me, 'events':events
			})
	else:
		messages.success(request,(" You aren't authorized to view this pase"))
		return redirect('home')	

def venue_csv(request):
	response= HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=venues.csv'
	
	#create a csv writer
	writer = csv.writer(response)

	#designate the model
	venues = Venue.objects.all()

	#add headings to the csv file
	writer.writerow(['Venue Name', 'Address','Zip Code', 'Phone', 'Web Address','email_address'])

	#loop thru and output
	for venue in venues:
		writer.writerow([venue.name,venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address ])
	return response


#generate Text file Venue
def venue_text(request):
	response= HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=venues.txt'
	#designate the model
	venues = Venue.objects.all()

	#create the list
	lines=[]
	#loop thru and output
	for venue in venues:
		lines.append(f'{venue.name}\n {venue.address}\n')

	#lines = ["this is line 1 \n",
	#"this is line 2 \n", 
	#"this is line 3 \n"]

	#write to TextFile
	response.writelines(lines)
	return response

#delete a venue

def delete_venue(request, venue_id):
	venue= Venue.objects.get(pk=venue_id)
	venue.delete()
	return redirect('list_venues')

#delete an event

def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user == event.manager:
		event.delete()
		return redirect('list-events')
		messages.success(request, "Event Deleted!!")
		
	else:
		messages.success(request, "access denied. you aren't authorized to delete this event")
		return redirect('list-events')

def update_Event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user.is_superuser:
		form = EventFormAdmin(request.POST or None, instance = event)
	else:
		form = EventForm(request.POST or None, instance = event)
	if form.is_valid():
		form.save()
		return redirect('list-events')
	return render(request, 'events/update_Event.html',
		{'event': event, 'form': form})

def Add_event(request):
	submitted=False 
	if request.method == "POST":
		if request.user.is_superuser:
			form = EventFormAdmin(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/Add_event?submitted=True')
		else:
			form= EventForm(request.POST)
			if form.is_valid():
				event = form.save(commit=False)
				event.manager=request.user #logged in user
				event.save()
				return HttpResponseRedirect('/Add_event?submitted=True')
	else:
		#Just going to the page, not submitting
		if request.user.is_superuser:
			form = EventFormAdmin
		else:
			form = EventForm
		if 'submitted' in request.GET:
			submitted= True
	return render(request, 'Events/Add_event.html',{'form': form,'submitted':submitted})

def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None,request.FILES or None, instance=venue, )
	if form.is_valid():
		form.save()
		return redirect('list_venues')
	return render(request, 'events/update_venue.html',
		{'venue': venue, 'form': form})

# delete an event

def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	event.delete()
	return redirect('list-events')

def search_events(request):
	if request.method=="POST":
		searched = request.POST['searched']
		events=Event.objects.filter(description__contains= searched)

		return render(request, 'events/search_events.html',
		{'searched':searched, 'events':events})
	else:
		return render(request, 'events/search_events.html',
		{})	
def search_venues(request):
	if request.method=="POST":
		searched = request.POST['searched']
		venues=Venue.objects.filter(name__contains= searched)

		return render(request, 'events/search_venues.html',
		{'searched':searched, 'venues':venues})
	else:
		return render(request, 'events/search_venues.html',
		{})	

def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue_owner = User.objects.get(pk=venue.owner)
	return render(request, 'events/show_venue.html',
		{'venue': venue, 'venue_owner': venue_owner})


def list_venues(request):
	#venue_list = Venue.objects.all().order_by('?')
	venue_list = Venue.objects.all()
	
	#set up pagination
	p = Paginator(Venue.objects.all(), 1)
	page = request.GET.get('page')
	venues = p.get_page(page)
	nums = "a" * venues.paginator.num_pages
	

	return render(request, 'events/venue.html',
		{'venue_list': venue_list,
		'venues':venues,'nums':nums})

def Add_venue(request):
	submitted=False 
	if request.method == "POST":
		form= VenueForm(request.POST, request.FILES)
		if form.is_valid():
			venue = form.save(commit=False)
			venue.owner=request.user.id #logged in user
			venue.save()
			#form.save()
			return HttpResponseRedirect('/add_venue?submitted=True')
	

	else:
		form = VenueForm
		if 'submitted' in request.GET:
			submitted= True
	return render(request, 'Events/Add_venue.html',{'form': form,'submitted':submitted})

def all_events(request):
	event_list = Event.objects.all().order_by('event_date')
	return render(request, 'Events/event_list.html',
		{'event_list':event_list})


# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):

	name ="John"
	month = month.title()
	#convert month from name to number
	month_number=list(calendar.month_name).index(month)
	month_number = int(month_number)

	#create a calender
	cal = HTMLCalendar().formatmonth(year, 
		month_number)
	#get current year
	now = datetime.now()
	current_year= now.year

	#Query the events model for Dates
	event_list = Event.objects.filter(

		event_date__year = year,
		event_date__month = month_number,

		)
	return render(request, 'events/home.html',{
		"name":name,
		"year":year,
		"month":month,
		"month_number":month_number,
		"cal":cal,
		"current_year":current_year,
		"event_list":event_list,

		})

