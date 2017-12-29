from django.conf.urls import url, include

from . import views


app_name = 'ResourceCentre'

# To do
# - Add sitemap
# - Update to Django 2.0

resource_patterns = [
    url(r"^$", views.ResourceView.as_view(), name="resource"),
    url(r"^/edit$", views.ResourceEditView, name="resource edit"),
]

category_patterns = [
    url(r"^$", views.CategoryLandingView.as_view(), name="category landing"),
    url(r"^(?P<external_id>[\w]{6})/(?P<slug>[\w-]+)", include(resource_patterns))
]

urlpatterns = [
    url(r"^$", views.ResourceCentreLandingView.as_view(), name="resource centre landing"),
    url(r"^risk-assessments/", include(category_patterns), {"category": "RiskAssessment"}),
    url(r"^activities/", include(category_patterns), {"category": "Activity"}),
    url(r"^meetings/", include(category_patterns), {"category": "Meeting"}),
    url(r"^camps/", include(category_patterns), {"category": "Camp"}),
]
