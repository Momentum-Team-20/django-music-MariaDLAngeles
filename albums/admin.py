from django.contrib import admin
from .models import Artist, Album

# Register your models here.
admin.site.register(Album)
# admin.site.register(Title)
admin.site.register(Artist)
# admin.site.register(CreatedDate)