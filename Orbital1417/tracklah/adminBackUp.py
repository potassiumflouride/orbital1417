from django.contrib import admin
from tracklah.models import CharPost
from tracklah.models import CharityProjects
from tracklah.models import *

class CharPostModelAdmin(admin.ModelAdmin):
    list_display = ["location", "updated","timestamp" ]
    class Meta:
        model = CharPost
class charityProjectsAdmin(admin.ModelAdmin):
    list_display=['chocoCode','projectName','charityName','country','lat','lng', 'shortDescrip']
    class Meta:
        model=CharityProjects

class testCharityName(admin.ModelAdmin):
    list_display= ["charityName1" ,"testimg"]
    class Meta:
        model= CharityName

class testProjects( admin.ModelAdmin):
    list_display= ['projectName1','desc', 'location', 'charityName1']
    class Meta:
        model= Projects
class testDonationCode( admin.ModelAdmin):
    list_display =[ 'donationCode', 'projectName1','charityName1']
    class Meta:
        model= DonationCode

admin.site.register(CharPost, CharPostModelAdmin)
admin.site.register(CharityProjects,charityProjectsAdmin)
admin.site.register(CharityName,testCharityName)
admin.site.register(Projects, testProjects)
admin.site.register(DonationCode, testDonationCode)
