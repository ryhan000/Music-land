from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Album, Song

# Register your models here.
admin.site.site_header = 'Music land'
admin.site.register(Album)
admin.site.register(Song)
admin.site.unregister(Group)
