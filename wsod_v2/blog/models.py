from django.db import models
from django.utils import timezone #This is for the date_posted var
from django.contrib.auth.models import User #This is for importing the users who created the posts

# Create your models here.
class Post(models.Model): #This makes a table in mysql and writes it for us
    title = models.CharField(max_length=100) #Title field has a max length of 100 characters
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class version(models.Model):
    version = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.version