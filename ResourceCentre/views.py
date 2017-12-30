from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.views import View

from . import models


def suggested_resources(user, quantity, category=[], **kwargs):
    return []

def related_resources(resource, quantity, category=[], **kwargs):
    return []

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
    """Mutli-view selection handler."""

    def __init__(keyword, options, delete_kw=True):
        """
        keyword - kwarg name | string
        options - key-value pair of kwarg value and view | dictionary
        delete_kw - Delete keyword pair from kwargs

        """
        self.keyword = keyword
        self.options = options
        self.delete_kw = delete_kw

    def __call__(request, *args, **kwargs):
        choice = kwargs[self.keyword]
        if self.delete_kw:
            del(kwargs[self.keyword])
        return self.options[choice](request, *args, **kwargs)


class ActivityView(View):
    template = "ResourceCentre/resources/activity.html"

    def get(request, external_id, slug):
        resource = get_object_or_404(models.Activity, external_id=external_id, slug=slug)
        related = []
        return render(request, self.template, {"resource": resource, "related": related_resources})


class MeetingView(View):
    template = "ResourceCentre/resources/meeting.html"

    def get(request, external_id, slug):
        resource = get_object_or_404(models.Meeting, external_id=external_id, slug=slug)
        related = []
        return render(request, self.template, {"resource": resource, "related": related_resources})


class CampView(View):
    template = "ResourceCentre/resources/camp.html"

    def get(request, external_id, slug):
        resource = get_object_or_404(models.Camp, external_id=external_id, slug=slug)
        related = []
        return render(request, self.template, {"resource": resource, "related": related_resources})


class RiskAssessmentView(View):
    template = "ResourceCentre/resources/risk-assessment.html"

    def get(request, external_id, slug):
        resource = get_object_or_404(models.RiskAssessment, external_id=external_id, slug=slug)
        related = []
        return render(request, self.template, {"resource": resource, "related": related_resources})


resource_view_divider = ViewDivider(
    "category",
    {
        "Activity": ActivityView.as_view(),
        "Meeting": MeetingView.as_view(),
        "Camp": CampView.as_view(),
        "RiskAssessment": RiskAssessment.as_view()
    }
)

#class ResourceEditView(View):
#    """Resource editing view."""
#
#    def get(self, request, category, external_id, slug):
#        pass
