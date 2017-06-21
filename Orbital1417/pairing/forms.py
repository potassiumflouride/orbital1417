from django import forms

from models import PairingSignupData

class PairingSignupform(forms.Form):
    '''
    name=forms.CharField (label='Your name', max_length=100)
    contact=forms.IntegerField (label='Your Phone Number')
    experiences=forms.TextField(label='Enter your relevant experience')
    created_date= forms.DateTimeField(default=timezone.now)
    '''

    class Meta:
        model= PairingSignupData
        fields = ('name', 'contact', 'experiences', 'created_date',)
