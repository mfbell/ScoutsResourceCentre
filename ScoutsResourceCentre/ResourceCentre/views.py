from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


def resources(request):
    return HttpResponse("Resource Centre landing page.")

def category(request, category):
    return HttpResponse("{} landing page.".format(category))

def resource(request, pk):
    return HttpResponse("Resource {} landing page.".format(pk))

def tree(request, pk):
    return HttpResponse("Resource {} relations tree view.".format(pk))
