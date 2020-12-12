from django.forms import ModelForm
from django import forms


from .models import Internship

class InternshipForm(ModelForm):
	class Meta:
		model = Internship
		fields = '__all__'