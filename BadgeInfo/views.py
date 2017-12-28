from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def landing_page(request):
    return HttpResponse("BadgeInfo landing page.")

def section(request, section):
    return HttpResponse("BadgeInfo {} landing page.".format(section))

def category(request, section, category):
    return HttpResponse("BadgeInfo {} {} landing page.".format(section, category))

def badge(request, section, category, badge):
    return HttpResponse("BadgeInfo {} {} {}.".format(section, category, badge))
