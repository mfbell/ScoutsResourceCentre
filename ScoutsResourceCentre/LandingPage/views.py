from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'LandingPage/home.html')

def ph_users(request):
    return HttpResponse("Users will be coming soon.")
