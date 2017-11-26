#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Scouts Resource Centre landing page.")
