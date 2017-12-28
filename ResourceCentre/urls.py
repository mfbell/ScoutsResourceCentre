from django.conf.urls import url, include

from . import views


app_name = 'ResourceCentre'

#resource_patterns = [
#    url(r"^$", ),
#    url(r"^/tree/$", views.tree, name="tree"),
#]

resource_by_pk_pattern = url(r"^(?P<external_id>[\w]{6})/(?P<slug>[\w-]+)", views.resource, name="resource")
#curated_resource_pattern = url(r"^(?P<pk>[\w-]+)/", include(resource_patterns))

category_patterns = [
    url(r"^$", views.category, name="category"),
    resource_by_pk_pattern,
]

urlpatterns = [
    url(r"^$", views.resources, name="resources"),
    url(r"^risk-assessments/", include(category_patterns), {"category": "riskassessments"}),
    url(r"^activities/", include(category_patterns), {"category": "activities"}),
    url(r"^meetings/", include(category_patterns), {"category": "meetings"}),
    url(r"^camps/", include(category_patterns), {"category": "camps"}),
    #curated_resource_pattern
]
