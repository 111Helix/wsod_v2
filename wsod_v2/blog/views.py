from django.shortcuts import render #This reduces the amount of code needed to render a view

# ─── INDEX PAGE ─────────────────────────────────────────────────────────────────
posts1 = [
    {
        "author": "111Helix",
        "title": "Toothpaste",
        "content": "Our newly added topic is toothpaste! Toothpaste is a vital necessity as we humans use it everyday in order to maintain our hygiene to a healthy standard. It's an abrasive that aids in removing dental plaque and food from the teeth, assists in suppressing halitosis and delivers active ingredients (most commonly fluoride) to help prevent tooth decay and gum disease.",
        "date_posted": "25/7/2020",
    }
]

posts2 = [
    {
        "author": "krisudom",
        "title": "Trombone",
        "content": "Trombone content",
        "date_posted": "25/7/2020",
    }
]

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

upInfo = [
    {
        "version": "Alpha 1.0.0",
        "content": "Alpha 1.0.0 content here",
    }
]

def index(request): #This is routes what users will see on the homepage
    context = { #context here allows the data (posts above) to be passed and accessed by the template
        "posts1": posts1, #This is the key for the context variable, allows this to be returned to the template
        "posts2": posts2, #Same as above ^^^
        "vote1": vote1,
        "vote2": vote2,
        "vote3": vote3,
        "upInfo": upInfo,
    }
    return render(request, "blog/index.html", context) #"blog/indexNonRegistered.html" = name_of_app/template_name_to_render
# ─── END INDEX PAGE ─────────────────────────────────────────────────────────────

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
