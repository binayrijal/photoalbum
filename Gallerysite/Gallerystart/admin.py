from django.contrib import admin
from .models import Album
# Register your models here.

@admin.register(Album)

class AlbumModelAdmin(admin.ModelAdmin):
    list_display=['id','user','photo','classification']