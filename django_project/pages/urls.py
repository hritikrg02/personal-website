from django.urls import path

from .views import (
    home_page_view,
    projects_page_view,
    thesis_page_view,
    photography_page_view,
    musescore_page_view,
)

# the route is the subdirectory based on what's in the django-project/urls.py
urlpatterns = [
    path("", home_page_view, name="home"),
    path("projects/", projects_page_view, name="projects"),
    path("thesis/", thesis_page_view, name="thesis"),
    path("musescore-engraving/", musescore_page_view, name="musescore-engraving"),
    path("photography/", photography_page_view, name="photography"),
]
