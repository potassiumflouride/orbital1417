from django.contrib import admin
from tracklah.models import CharPost
from tracklah.models import CharityProjects

class CharPostModelAdmin(admin.ModelAdmin):
    list_display = ["location", "updated","timestamp" ]
    class Meta:
        model = CharPost
class charityProjectsAdmin(admin.ModelAdmin):
    list_display=['projectName','charityName','country','lat','lng']
    class Meta:
        model=CharityProjects

admin.site.register(CharPost, CharPostModelAdmin)
admin.site.register(CharityProjects,charityProjectsAdmin)
