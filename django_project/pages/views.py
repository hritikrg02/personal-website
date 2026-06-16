from django.shortcuts import render

# Create your views here.


def home_page_view(request):  # function-based view
    return render(request, "home.html")


def about_page_view(request):
    cxt = {
        "name": "Ricky",
        "age": "24",
    }  # this is usually loaded via the model and gotten through the database
    return render(request, "about.html", cxt)
