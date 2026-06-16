from django.urls import path

from .views import home_page_view, AboutPageView

# the route is the subdirectory based on what's in the django-project/urls.py
urlpatterns = [
    path(
        "", home_page_view, name="home"
    ),
    path(
        "about/", AboutPageView.as_view(), name="about"
    )
]
