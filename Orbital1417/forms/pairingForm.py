from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.http import HttpResponse, request

from forms import forms


class PairingSignupform(request):
    class Meta:
        model=User
        fields= ('Name','Contact_Number', 'experiences',)
