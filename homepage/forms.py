from django import forms
from django.forms import ModelForm
from .models import contactForm
from .models import Survey
# create form

class ContactFormForm(ModelForm):
	class Meta:
		model = contactForm
		fields = ('email', 'name', 'title', 'description')