from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views import View

from . import models
from . import forms


def homepage(request):
    return render(request, "ResourceCentre/homepage.html")

def resources(request):
    return render(request, "ResourceCentre/resources.html")

def create(request):
    return render(request, "ResourceCentre/create.html")

class Resource(View):
    templates = {
        models.Activity: "ResourceCentre/activity.html",
        models.RiskAssessment: "ResourceCentre/risk-assessment.html"
    }

    def get(self, request, slug):
        resource = get_object_or_404(models.ResourceSlug, slug=slug).resource
        return render(request, self.templates[type(resource)], {"resource": resource})

    def post(self, request, slug):
        resource = get_object_or_404(models.ResourceSlug, slug=slug).resource
