from django.urls import path
from . import views #The . here is signifying that it's on the current directory

urlpatterns = [
    path("", views.index, name="blog_index"), #views.index = name_of_file(without.py).name_of_function
    path("news/", views.news, name="blog_news")
]
