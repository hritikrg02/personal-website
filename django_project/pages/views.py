from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    return render(request, "home.html")


def projects_page_view(request):
    return render(request, "projects.html")

def work_page_view(request):
    return render(request, "work.html")


def musescore_page_view(request):
    return render(request, "musescore-engraving.html")


def photography_page_view(request):
    return render(request, "photography.html")


def thesis_page_view(request):
    return render(request, "thesis.html")
