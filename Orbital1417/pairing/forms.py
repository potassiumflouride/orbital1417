from django import forms

from models import PairingSignupData

class PairingSignupform(forms.ModelForm):


    class Meta:
        model= PairingSignupData
        fields = ('name', 'contact', 'experiences', 'created_date',)
