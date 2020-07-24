from django.urls import path
from . import views #The . here is signifying that it's on the current directory

urlpatterns = [
    path("", views.index, name="blog_index"), #views.index = name_of_file(without.py).name_of_function
    path("verHistory/", views.verHistory, name="blog_verHistory"),
    path("bugFix/", views.bugFix, name="blog_bugFix"),
    path("voteResults/", views.voteResults, name="blog_voteResults"),
    path("roadMap/", views.roadMap, name="blog_roadMap"),
]
