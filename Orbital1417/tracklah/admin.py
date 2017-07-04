from django.contrib import admin
from tracklah.models import CharPost

class CharPostModelAdmin(admin.ModelAdmin):
    list_display = ["location", "updated","timestamp" ]
    class Meta:
        model = CharPost

admin.site.register(CharPost, CharPostModelAdmin)
