from django.contrib import admin
from tracklah.models import *

class CharityOrgAdmin (admin.ModelAdmin):
    list_display = [ "charityName", "address","postalCode", "contactNum", "emailAddr"]
    class Meta:
        model = CharityOrg

class CharityProjMainAdmin (admin.ModelAdmin):
    list_display = [ "projectNameMain","charityName","projectDir","dateStarted", "dateCompleted"]
    class Meta:
        model = CharityProjMain


class CharityProjSubAdmin (admin.ModelAdmin):
    list_display = [ "projectNameSub","projectNameMain","charityName", "shortWriteup", "infoWindowWriteup", "country", "city", "lat"
                    ,"lng","zoom","dateStarted", "dateCompleted",
                    "img1", "img2","img3", "videoLink"]
    class Meta:
        model = CharityProjSub

class ChocoCodeAdmin (admin.ModelAdmin):
    list_display = [ "donationCode", "projectNameSub","projectNameMain",
                    "charityOrg", "maxNumUsers", "currNumUser"]
    class Meta:
        model = ChocoCode



admin.site.register(CharityOrg, CharityOrgAdmin)
admin.site.register(CharityProjMain, CharityProjMainAdmin)
admin.site.register(CharityProjSub, CharityProjSubAdmin)
admin.site.register(ChocoCode, ChocoCodeAdmin)
