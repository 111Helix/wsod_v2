from django.shortcuts import render #This reduces the amount of code needed to render a view

# Create your views here.
def index(request): #This is routes what users will see on the homepage
    return render(request, "blog/index.html") #"blog/indexNonRegistered.html" = name_of_app/template_name_to_render

def verHistory(request):
    return render(request, "blog/verHistory.html")

def bugFix(request):
    return render(request, "blog/bugFix.html")

def voteResults(request):
    return render(request, "blog/voteResults.html")

def roadMap(request):
    return render(request, "blog/roadMap.html")

def aboutUs(request):
    return render(request, "blog/aboutUs.html")

def docs(request):
    return render(request, "blog/docs.html")
