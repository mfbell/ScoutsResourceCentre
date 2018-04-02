from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views import View
from django.urls import reverse

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


class EditActivity(View):
    template = "ResourceCentre/edit-resource.html"

    def get(self, request, slug, resource):
        activity_form = forms.ActivityForm(instance=resource)
        activitystage_formset = forms.ActivityStageInlineFormSet(instance=resource)
        return render(
            request,
            self.template,
            {
                "activity_form": activity_form,
                "activitystage_formset": activitystage_formset
            }
        )

    def post(self, request, slug, resource):
        activity_form = forms.ActivityForm(request.POST, instance=resource)
        activitystage_formset = forms.ActivityStageInlineFormSet(request.POST, instance=resource)
        if activity_form.is_valid() and activitystage_formset.is_valid():
            activity_form.save()
            activitystage_formset.save()
            return HttpResponseRedirect(reverse("ResourceCentre:resource", args=(slug,)))

        return render(
            request,
            self.template,
            {
                "activity_form": activity_form,
                "activitystage_formset": activitystage_formset
            }
        )


class EditRiskAssessment(View):
    template = "ResourceCentre/edit-resource.html"

    def get(self, request, slug, resource):
        pass

    def post(self, request, slug, resource):
        pass


class EditResourceSplitter:
    views = {
        models.Activity: EditActivity.as_view(),
        models.RiskAssessment: EditRiskAssessment.as_view()
    }

    def __call__(self, request, slug):
        resource = get_object_or_404(models.ResourceSlug, slug=slug).resource
        return self.views[type(resource)](request, slug, resource)
