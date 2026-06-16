from django.urls import path

from .views import home_page_view

urlpatterns = [
    path(
        "", home_page_view
    )  # the route is the subdirectory based on what's in the django-project/urls.py
]
