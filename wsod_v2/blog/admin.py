from django.contrib import admin
from . models import Post, version

# Register your models here.
admin.site.register(Post) #Allows the admin page to show the posts
admin.site.register(version)