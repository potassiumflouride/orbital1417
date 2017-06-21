# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# database for details of the charity job listing
class Pairing (models.Model):
    charityName = models.CharField(primary_key=True,max_length=20)
    title = models.CharField(max_length=200)
    text= models.TextField()
    created_date= models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #image?
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PairingSignupData (models.Model):
    name= models.CharField(max_length=20)
    contact= models.IntegerField()
    experiences= models.TextField()
    created_date= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
