from django.shortcuts import render

# Create your views here.


def home_page_view(request):  # function-based view
    return render(request, "home.html")


