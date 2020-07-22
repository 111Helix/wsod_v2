from django.shortcuts import render #This reduces the amount of code needed to render a view
from django.http import HttpResponse

# Create your views here.
def index(request): #This is routes what users will see on the homepage
    return render(request, "blog/indexNonRegistered.html") #"blog/indexNonRegistered.html" = name_of_app/template_name_to_render