from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone


def upload_location(Charity, filename):
    return "%s/%s" %(Charity.title, filename)

class Post(models.Model):
    #model_pic = models.ImageField(upload_to = 'charity/static/img/', default = 'static/img/None/no-img.jpg', null= True, blank =True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    mission = models.TextField(null= True, blank =True)
    vision = models.TextField(null= True, blank =True)
    width_field=models.IntegerField(default=0)
    height_field=models.IntegerField(default=0)
    img = models.ImageField(upload_to=upload_location,
                                blank=True, null=True,
                                width_field="width_field",
                                height_field="height_field",
                                )
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
