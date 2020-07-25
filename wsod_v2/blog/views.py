from django.shortcuts import render #This reduces the amount of code needed to render a view
from . models import Post, version

# ─── INDEX PAGE ─────────────────────────────────────────────────────────────────
vote1 = [
    {
        "topic": "Vote topic1",
        "info": "Add description here"
    }
]

vote2 = [
    {
        "topic": "Vote topic2",
        "info": "Add description here"
    }
]

vote3 = [
    {
        "topic": "Vote topic3",
        "info": "Add description here"
    }
]

def index(request): #This is routes what users will see on the homepage
    context = { #context here allows the data (posts above) to be passed and accessed by the template
        "posts": Post.objects.all().order_by("-date_posted")[:1],#Post.objects.all(),#Post.objects.all().order_by("-date_posted")[0], #This is the key for the context variable, allows this to be returned to the template
        "vote1": vote1,
        "vote2": vote2,
        "vote3": vote3,
        "version": version.objects.all().order_by("-date_posted")[0]
    }
    return render(request, "blog/index.html", context) #"blog/indexNonRegistered.html" = name_of_app/template_name_to_render
# ─── END INDEX PAGE ─────────────────────────────────────────────────────────────

# ─── VERSION HISTORY PAGE ───────────────────────────────────────────────────────
def verHistory(request):
    context = {
        "version": version.objects.all().order_by("-date_posted")
    }
    return render(request, "blog/verHistory.html", context)

# ─── END VERSION HISTORY PAGE ───────────────────────────────────────────────────

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
