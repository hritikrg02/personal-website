from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

# TODO decide which kind of view I want to use for the website, I'm thinking objects but part of me wants to do functions

def home_page_view(request):  # function-based view
    return render(request, "home.html")

# def about_page_view(request):
#     cxt = {"name": "Ricky", "age": "24"}  # this is usually loaded via the model and gotten through the database
#     return render(request, "about.html", cxt)

class AboutPageView(TemplateView):  # generic class-based view
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Ricky"
        context["age"] = "24"
        return context