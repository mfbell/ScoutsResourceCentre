from django.conf.urls import url, include

from . import views


app_name = 'LandingPage'
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^users/$", views.ph_users, name="users"),
]
