# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pairing.models import Pairing, PairingSignupData


#admin.site.register(Pairing)


#pairing blog post
class PairingAdmin(admin.ModelAdmin):
    search_fields= ['jobcode','charityName', 'title', 'created_date','published_date','text']
    list_display= ('jobcode','published_date','charityName')
    fields= ['jobcode','charityName', 'title', 'created_date','published_date','text']
    list_display= ('jobcode','published_date','charityName')
    list_filter= ['jobcode','published_date','charityName']

admin.site.register(Pairing, PairingAdmin)


# pairing signup forms
class pairingSignupAdmin(admin.ModelAdmin):
    list_display= ['jobcode','name','contact','email','experiences',]
    fields= ['jobcode','name','contact','email','experiences',]


admin.site.register(PairingSignupData, pairingSignupAdmin)
