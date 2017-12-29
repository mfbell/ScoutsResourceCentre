from django.urls import path, include

from . import views


app_name = 'ResourceCentre'

# To do
# - Add sitemap

resource_patterns = [
    path("", views.ResourceView.as_view(), name="resource"),
    path("edit", views.ResourceEditView.as_view(), name="resource-edit"),
]

category_patterns = [
    path("", views.CategoryLandingView.as_view(), name="category-landing"),
    path("<str:external_id>/<slug:slug>/", include(resource_patterns))
]

urlpatterns = [
    path("", views.ResourceCentreLandingView.as_view(), name="resource-centre-landing"),
    path("risk-assessments/", include(category_patterns), {"category": "RiskAssessment"}),
    path("activities/", include(category_patterns), {"category": "Activity"}),
    path("meetings/", include(category_patterns), {"category": "Meeting"}),
    path("camps/", include(category_patterns), {"category": "Camp"}),
]
