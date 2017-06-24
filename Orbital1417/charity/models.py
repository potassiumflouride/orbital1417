from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone

class Post(models.Model):
    model_pic = models.ImageField(upload_to = 'charity/static/img/', default = 'static/img/None/no-img.jpg', null= True, blank =True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
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
