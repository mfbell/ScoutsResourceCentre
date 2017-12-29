from django.shortcuts import get_object_or_404, render
from django.http import Http404
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
        # To add
        # - search system? or suggested content
        return render(request, "ResourceCentre/category-landing.html", {"category": category})


class ViewDivider:
    """"""

    def __init__(keyword, options, delete_kw=True):
        self.keyword = keyword
        self.options = options
        self.delete_kw = delete_kw

    def view(request, *args, **kwargs):
        choice = kwargs[self.keyword]
        if self.delete_kw:
            del(kwargs[self.keyword])
        return self.options[choice](request, *args, **kwargs)


class ActivityView(View):
    def get(request, external_id, slug):
        resource = get_object_or_404(models.Activity, external_id=external_id, slug=slug)
        template = "ResourceCentre/resources/activity.html"
        return render(request, template, {"resource": resource, "related": related_resources})


class MeetingView(View):
    def get(request, external_id, slug):
        resource = get_object_or_404(models.Meeting, external_id=external_id, slug=slug)
        template = "ResourceCentre/resources/meeting.html"
        return render(request, template, {"resource": resource, "related": related_resources})


class CampView(View):
    def get(request, external_id, slug):
        resource = get_object_or_404(models.Camp, external_id=external_id, slug=slug)
        template = "ResourceCentre/resources/camp.html"
        return render(request, template, {"resource": resource, "related": related_resources})


class RiskAssessmentView(View):
    def get(request, external_id, slug):
        resource = get_object_or_404(models.RiskAssessment, external_id=external_id, slug=slug)
        template = "ResourceCentre/resources/risk-assessment.html"
        return render(request, template, {"resource": resource, "related": related_resources})


class ResourceEditView(View):
    """Resource editing view."""

    def get(self, request, category, external_id, slug):
        pass
