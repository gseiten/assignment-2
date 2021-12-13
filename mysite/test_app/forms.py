# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Company

User = get_user_model()


class UserForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname',
                  'phone_number', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'phone_number')


class CompanyUpdateForm(forms.ModelForm):
    name = forms.CharField()
    location = forms.CharField()
    website = forms.URLField()
    employee = User

    class Meta:
        model = Company
        fields = ('name', 'location', 'website')
