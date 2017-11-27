from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def resources(request):
    return HttpResponse("Resource Centre landing page.")

def riskassessments(request):
    return HttpResponse("Risk assessments landing page.")

def activities(request):
    return HttpResponse("Activities landing page.")

def meetings(request):
    return HttpResponse("Meetings landing page.")

def camps(request):
    return HttpResponse("Camps landing page.")

def resource(request, pk):
    return HttpResponse("Resource {} landing page.".format(pk))
