from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone

def upload_location(CharPost, filename):
    return "%s/%s" %(CharPost.title, filename)

class CharPost(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    donor = models.CharField(max_length=200)
    benef = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    text = models.TextField()
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    clat = models.CharField(max_length=200, blank=True, null=True)
    clng =  models.CharField(max_length=200, blank=True, null=True)
    '''img1 = models.ImageField(upload_to=upload_location,
                            blank=True, null=True,
                            width_field="width_field",
                            height_field="height_field",
                            )
    img2 = models.ImageField(upload_to=upload_location,
                            blank=True, null=True,
                            width_field="width_field",
                            height_field="height_field",
                            )
                            '''

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null= True, blank =True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null= True, blank =True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class CharityProjects(models.Model):
    chocoCode= models.CharField(max_length=200, blank=True, null=True)
    projectName= models.CharField(max_length=200, blank=True, null=True)
    charityName= models.CharField(max_length=200, blank=True, null=True)
    country= models.CharField(max_length=200, blank=True, null=True)
    lat= models.CharField(max_length=200, blank=True, null=True)
    lng= models.CharField(max_length=200, blank=True, null=True)

    
