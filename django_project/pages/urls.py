from django.urls import path

from .views import home_page_view, about_page_view

# the route is the subdirectory based on what's in the django-project/urls.py
urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", about_page_view, name="about"),
]
