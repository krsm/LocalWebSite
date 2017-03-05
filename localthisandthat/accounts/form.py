from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    # A widget is Django’s representation of an HTML input element
    password = forms.CharField(widget=forms.PasswordInput())
    # Anything within a nested Meta class describes additional properties
    # about the particular class to which it belongs

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('zip', 'state', 'city', 'address_1', 'address_2')

