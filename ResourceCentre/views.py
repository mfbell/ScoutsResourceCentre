from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import View

from . import models
# Activity, Meeting, Camp, RiskAssessment

class ResourceCentreLandingView(View):
    """Resource centre laning page view."""

    def get(self, request):
        return HttpResponse("Resource Centre landing page.")


class ResourceView(View):
    """Processesing requests of detailed resources views."""

    # Needs better design to decouple layers.
    def get(self, request, category, external_id, slug):
        if category == "activities":
            resource = get_object_or_404(models.Activity, external_id=external_id, slug=slug)
        elif category == "meetings":
            resource = get_object_or_404(models.Meeting, external_id=external_id, slug=slug)
        elif category == "camps":
            resource = get_object_or_404(models.Camp, external_id=external_id, slug=slug)
        elif category == "risk-assessments":
            resource = get_object_or_404(models.RiskAssessment, external_id=external_id, slug=slug)
        else:
            pass

def category(request, category):
    return HttpResponse("{} landing page.".format(category))

def resource(request, ):
    if category == "activity":
        resource =  get_object_or_404(models.Activity, external_id=external_id)
    #return render(request, 'ResourceCentre/resource.html', {"title": slug, "description": external_id, "category": category})
        return HttpResponse("Resource {} landing page. {} {}\n{}".format(slug, external_id, category, dir(resource)))
    else:
        return HttpResponse("Unknown")

def tree(request, pk):
    return HttpResponse("Resource {} relations tree view.".format(pk))
