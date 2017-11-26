from uuid import uuid4

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models



def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

def get_sentinel_parent():
    return

class Resource(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        help_text="Unique ID",
    )
    title = models.CharField(
        max_length=128,
        help_text="A short, one-point title for your resource.",
    )
    desciption = models.TextField(help_text="What is your resource?")
    beavers = models.BooleanField(
        default=False,
        help_text="Is your resource aimed at the Beaver section?",
    )
    cubs = models.BooleanField(
        default=False,
        help_text="Is your resource aimed at the Cub section?",
    )
    scouts = models.BooleanField(
        default=True,
        help_text="Is your resource aimed at the Scout section?",
    )
    explorers = models.BooleanField(
        default=False,
        help_text="Is your resource aimed at the Explorer section?",
    )
    network = models.BooleanField(
        default=False,
        help_text="Is your resource aimed at the Beavers section?",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text="Date-time created.",
    )
    updated = models.DateTimeField(
        auto_now=True,
        help_text="Date-time updated.",
    )
    curated = models.BooleanField(
        default=False,
        help_text="Is the resource curated? Results in extra protection and restrictions.",
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        editable=False,
        help_text="The orginal creator.",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    editors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    PUBLIC = "PU"
    HIDEN = "HI"
    VISIBILITIES = (
        (PUBLIC, "Public"),
        (HIDEN, "Only you - hiden"),
    )
    visibility = models.CharField(
        max_length=2,
        choices=VISIBILITIES,
        default=PUBLIC,
        help_text="Who the resource is visibly to.",
    )
    parent = models.ForeignKey(
        'self',
        blank=True
        on_delete=models.SET(get_sentinel_parent)
        help_text="If the resource for copied and edited, the parent.",
    )
    #children from parent?
    #generated_from future feature
    views = IntegerField(default=0)
    #likes from ForeignKey
    #saves from ForeignKey

    class Meta:
        abstract = True
