from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone


def upload_location(CharityProjSub, filename):
    return "%s/%s" %(CharityProjSub.projectNameSub, filename)



class CharityOrg (models.Model):
    charityName = models.CharField(max_length=200, blank=False, null=False, primary_key=True)
    address = models.CharField(max_length=200, blank=False, null=True)
    postalCode= models.IntegerField()
    contactNum = models.IntegerField()
    emailAddr = models.EmailField(max_length=70,blank=False)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.charityName

class CharityProjMain (models.Model):
    projectNameMain= models.CharField( max_length=200,blank=False,null=False, primary_key=True)
    charityName= models.ForeignKey(CharityOrg)
    projectDir= models.CharField( max_length=200,blank=False,null=True)
    dateStarted= models.DateField(blank=False,null=True)
    dateCompleted= models.DateField(blank=False,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.projectNameMain



class CharityProjSub (models.Model):
    projectNameSub= models.CharField(max_length=200,blank=False,null=False, primary_key=True)
    projectNameMain= models.ForeignKey(CharityProjMain)
    charityName= models.ForeignKey(CharityOrg)
    shortWriteup= models.TextField(blank=False,null=True)
    infoWindowWriteup= models.TextField(blank=False,null=True)
    country= models.CharField(max_length=200,blank=False,null=True)
    city= models.CharField(max_length=200,blank=False,null=True)
    lat= models.FloatField(max_length=200, blank=False, null=True)
    lng= models.FloatField(max_length=200, blank=False, null=True)
    zoom= models.IntegerField()
    dateStarted= models.DateField(blank=False,null=True)
    dateCompleted= models.DateField(blank=False,null=True)
    img1 = models.ImageField(upload_to=upload_location,
                            blank=True, null=True,
                            )
    img2 = models.ImageField(upload_to=upload_location,
                            blank=True, null=True,
                            )
    img3 = models.ImageField(upload_to=upload_location,
                            blank=True, null=True,
                            )

    videoLink = models.URLField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.projectNameSub

class ChocoCode (models.Model):
    donationCode= models.CharField(max_length=200,blank=False,null=False, primary_key=True)
    projectNameSub= models.ForeignKey(CharityProjSub)
    projectNameMain= models.ForeignKey(CharityProjMain)
    charityOrg= models.ForeignKey(CharityOrg)
    currNumUser= models.IntegerField(default=1)
    maxNumUsers=models.IntegerField(default=1)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.donationCode
