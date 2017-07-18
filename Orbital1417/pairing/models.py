# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm


# Create your models here.
def upload_location(Pairing, filename):
    return "%s/%s" %(Pairing.charityName, filename)

# database for details of the charity job listing
class Pairing (models.Model):
    charityName = models.CharField(primary_key=True ,max_length=20)
    jobcode = models.IntegerField(null=True,blank=True)
    title = models.CharField(max_length=200)
    width_field=models.IntegerField(default=0)
    height_field=models.IntegerField(default=0)
    img = models.ImageField(upload_to=upload_location,
                            blank=True, null=True,
                            width_field="width_field",
                            height_field="height_field",
                            )
    text= models.TextField()
    created_date= models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PairingSignupData (models.Model):
    name= models.CharField(primary_key=True,max_length=20)
    jobcode = models.IntegerField(null=True,blank=True)
    email= models.EmailField(null=True,blank=True)
    contact= models.IntegerField(null=True,blank=True)
    experiences= models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


'''
class PairingSignupform(ModelForm):

    name= forms.CharField(help_text='Enter your name')
    contact= forms.IntegerField()
    experiences= forms.CharField(help_text='Enter your experiences')

    class Meta:
        model= PairingSignupData
        fields=['name', 'contact', 'experiences'] '''
