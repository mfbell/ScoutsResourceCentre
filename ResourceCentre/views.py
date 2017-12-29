from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.views import View

from . import models


class ResourceCentreLandingView(View):
    """Resource centre laning page view."""

    def get(self, request):
        # To add
        # - Suggested content
        return render(request, "ResourceCentre/landing.html")


class CategoryLandingView(View):
    """Resource category landing page."""

    def get(request, category):
        return render(request, "ResourceCentre/category-landing.html", {"category": category})


class ResourceView(View):
    """Processesing requests of detailed resources views."""

    # Needs better design to decouple layers.
    def get(self, request, category, external_id, slug):
        if category == "Activity":
            resource = get_object_or_404(models.Activity, external_id=external_id, slug=slug)
            template = "ResourceCentre/resources/activity.html"
        elif category == "Meeting":
            resource = get_object_or_404(models.Meeting, external_id=external_id, slug=slug)
            template = "ResourceCentre/resources/meeting.html"
        elif category == "Camp":
            resource = get_object_or_404(models.Camp, external_id=external_id, slug=slug)
            template = "ResourceCentre/resources/camp.html"
        elif category == "RiskAssessment":
            resource = get_object_or_404(models.RiskAssessment, external_id=external_id, slug=slug)
            template = "ResourceCentre/resources/risk-assessment.html"
        else:
            raise Http404
        # To add
        # - record users' views
        # - related resources
        return render(request, template, {'resource': resource})
