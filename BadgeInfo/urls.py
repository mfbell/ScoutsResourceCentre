from django.conf.urls import url, include

from . import views


app_name = 'BadgeInfo'

badge_patterns = [
    url(r"^$", views.badge, name="badge"),
]

badges_patterns = [
    url(r"^$", views.category, name="category"),
    url(r"^(?P<badge>[\w-]+)/", include(badge_patterns)),
]

badge_cat_patterns = [
    url(r"^$", views.section, name="section"),
    url(r"^core/", include(badges_patterns), {"category": "core"}),
    url(r"^challenge/", include(badges_patterns), {"category": "challenge"}),
    url(r"^activity/", include(badges_patterns), {"category": "activity"}),
    url(r"^staged/", include(badges_patterns), {"category": "staged"}),
    url(r"^awards/", include(badges_patterns), {"category": "awards"}),
]

urlpatterns = [
    url(r"^$", views.landing_page, name="landing_page"),
    url(r"^beavers/", include(badge_cat_patterns), {"section": "beavers"}),
    url(r"^cubs/", include(badge_cat_patterns), {"section": "cubs"}),
    url(r"^scouts/", include(badge_cat_patterns), {"section": "scouts"}),
    url(r"^explorers/", include(badge_cat_patterns), {"section": "explorers"}),
    url(r"^network/", include(badge_cat_patterns), {"section": "network"}),
]
