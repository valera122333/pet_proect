from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password1']


 
from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['title', 'description', 'image', 'data']
