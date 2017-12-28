from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from . import models
# Activity, Meeting, Camp, RiskAssessment


def resources(request):
    return HttpResponse("Resource Centre landing page.")

def category(request, category):
    return HttpResponse("{} landing page.".format(category))

def resource(request, category, external_id, slug):
    if category == "activity":
        resource = get_object_or_404(models.Activity, external_id=external_id)
    #return render(request, 'ResourceCentre/resource.html', {"title": slug, "description": external_id, "category": category})
        return HttpResponse("Resource {} landing page. {} {}\n{}".format(slug, external_id, category, dir(resource)))
    else:
        return HttpResponse("Unknown")

def tree(request, pk):
    return HttpResponse("Resource {} relations tree view.".format(pk))
