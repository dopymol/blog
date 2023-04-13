from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blogForm(ModelForm):
    class Meta:
        model=Blogs
        fields='__all__'
        exclude=['likes','date']



class UserRegistrationForm(UserCreationForm):
	first_name = forms.CharField(max_length=101)
	last_name = forms.CharField(max_length=101)
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username","first_name", "last_name", "email", "password", "password1"]