from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MHPSignUpForm(UserCreationForm):
    first = forms.CharField(label="First Name")
    last = forms.CharField(label="Last Name")
    field_order = ['first', 'last', 'username', 'password1', 'password2']
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
