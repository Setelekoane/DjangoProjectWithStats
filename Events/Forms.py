from django import forms
from django.forms import ModelForm
from .models import Venue


#create a venue form

class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields =('name','address','zip_code','phone',
			'email_address','web')
		labels={
			'name':'',
			'address':'',
			'zip_code':'',
			'phone':'',
			'email_address':'',
			'web':'',
			}
		widgets={

			'name':forms.TextInput(attrs={'class':'form-control','Placeholder':'Venue Name'}),
			'address':forms.TextInput(attrs={'class':'form-control','Placeholder':'Address'}),
			'zip_code':forms.TextInput(attrs={'class':'form-control','Placeholder':'Zip Code'}),
			'phone':forms.TextInput(attrs={'class':'form-control','Placeholder':'Phone'}),
			'email_address':forms.EmailInput(attrs={'class':'form-control','Placeholder':'Email Address'}),
			'web':forms.TextInput(attrs={'class':'form-control','Placeholder':'Email'}),

		}