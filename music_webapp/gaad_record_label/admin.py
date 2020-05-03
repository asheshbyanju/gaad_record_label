from django.contrib import admin
from .models import Artist
from .models import Album

# Register your models here.

admin.site.register(Artist)
admin.site.register(Album)

