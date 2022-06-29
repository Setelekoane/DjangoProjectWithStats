from django import forms
from django.forms import ModelForm
from .models import Venue, Event


#create a venue form

class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields =('name','address','zip_code','phone',
			'email_address','web','venue_image')
		labels={
			'name':'',
			'address':'',
			'zip_code':'',
			'phone':'',
			'email_address':'',
			'web':'',
			'venue_image':'',
			}
		widgets={

			'name':forms.TextInput(attrs={'class':'form-control','Placeholder':'Venue Name'}),
			'address':forms.TextInput(attrs={'class':'form-control','Placeholder':'Address'}),
			'zip_code':forms.TextInput(attrs={'class':'form-control','Placeholder':'Zip Code'}),
			'phone':forms.TextInput(attrs={'class':'form-control','Placeholder':'Phone'}),
			'email_address':forms.EmailInput(attrs={'class':'form-control','Placeholder':'Email Address'}),
			'web':forms.TextInput(attrs={'class':'form-control','Placeholder':'Website'}),

		}
#Admin Super User Event Form 
class EventFormAdmin(ModelForm):
	class Meta:
		model = Event
		fields =('name','event_date','venue','manager',
			'attendees','description',)
		labels={
			'name':'',
			'event_date':'YYYY-MM-DD HH:MM:SS',
			'venue':'Venue',
			'manager':'Manager',
			'attendees':'Attendees',
			'description':'',
			}
		widgets={

			'name':forms.TextInput(attrs={'class':'form-control','Placeholder':'Event Name'}),
			'event_date':forms.TextInput(attrs={'class':'form-control','Placeholder':'Event date'}),
			'venue':forms.Select(attrs={'class':'form-select','Placeholder':'Venue'}),
			'manager':forms.Select(attrs={'class':'form-select','Placeholder':'Manager'}),
			'attendees':forms.SelectMultiple(attrs={'class':'form-control','Placeholder':'Attendees'}),
			'description':forms.Textarea(attrs={'class':'form-control','Placeholder':'Description'}),
			

		}
# User Event Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields =('name','event_date','venue',
			'attendees','description',)
		labels={
			'name':'',
			'event_date':'YYYY-MM-DD HH:MM:SS',
			'venue':'Venue',
			'attendees':'Attendees',
			'description':'',
			}
		widgets={

			'name':forms.TextInput(attrs={'class':'form-control','Placeholder':'Event Name'}),
			'event_date':forms.TextInput(attrs={'class':'form-control','Placeholder':'Event date'}),
			'venue':forms.Select(attrs={'class':'form-select','Placeholder':'Venue'}),
			'attendees':forms.SelectMultiple(attrs={'class':'form-control','Placeholder':'Attendees'}),
			'description':forms.Textarea(attrs={'class':'form-control','Placeholder':'Description'}),
			

		}