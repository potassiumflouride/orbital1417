from django import forms

from pairing.models import PairingSignupData

from django.forms import ModelForm



class PairingSignupform(forms.ModelForm):

    class Meta:
        model= PairingSignupData
        fields= ('name','jobcode','contact','email','experiences',)
