from django.conf.urls import url, include

from . import views


app_name = 'ResourceCentre'

resource_patterns = [
    url(r"^$", views.resource, name="resource"),
    url(r"^tree/$", views.tree, name="tree"),
]

resource_pattern = url(r"^(?P<pk>[a-fA-F0-9]{32})/", include(resource_patterns))

riskassessments_patterns = [
    url(r"^$", views.riskassessments, name="riskassessments"),
    resource_pattern,
]

activities_patterns = [
    url(r"^$", views.activities, name="activities"),
    resource_pattern,
]

meetings_patterns = [
    url(r"^$", views.meetings, name="meetings"),
    resource_pattern,
]

camps_patterns = [
    url(r"^$", views.camps, name="camps"),
    resource_pattern,
]

urlpatterns = [
    url(r"^$", views.resources, name="resources"),
    url(r"^riskassessments/", include(riskassessments_patterns)),
    url(r"^activities/", include(activities_patterns)),
    url(r"^meetings/", include(meetings_patterns)),
    url(r"^camps/", include(camps_patterns)),
]
