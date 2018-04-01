from django.urls import path, include

from . import views


app_name = 'ResourceCentre'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("resources/", views.resources, name="resources"),
    path("resources/<slug:slug>", views.Resource.as_view(), name="resource"),
    path("create", views.create, name="create"),
]
