"""Base models."""

import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


def get_sentinel_user():
    """Get sentinel user."""
    return get_user_model().objects.get_or_create(username='deleted')[0]

def get_sentinel_parent():
    """Get sentinel parent."""
    sentinel = Resource.objects.get_or_create(
        id=uuid.uuid("847efe04e7484568910193961dd191ff"),
        title='deleted'
    )[0]
    return sentinel

class Resource(models.Model):
    """Base resource model."""
    RESOURCE_NAME = "resource"
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(
        max_length=128,
        help_text="A short, one-point title for your resources.",
    )
    desciption = models.TextField(help_text="Summerise  your resources.")
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
        related_name="created_resources",
        related_query_name="created_resource",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        help_text="The resource owner.",
        related_name="owned_resources",
        related_query_name="owned_resource",
    )
    editors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        help_text="Users with permission to edit the resource.",
        related_name="editor_roles",
        related_query_name="editor_role",
    )
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        help_text="Users who have contributed to the resource.",
        related_name="contributions",
        related_query_name="contribution",
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
        blank=True,
        on_delete=models.SET(get_sentinel_parent),
        help_text="For if the resource was a copy and edited, the parent.",
        related_name="children",
        related_query_name="child",
    )
    views = models.IntegerField(default=0)
    #generated_from future feature

    """
    def children(self):
        #children from parent?
        pass

    @property
    def likes(self):
        #likes from ForeignKey
        return likes

    @property
    def saves(self):
        #saves from ForeignKey
        return saves
    """

    def __str__(self):
        return "Base resource model"

    class Meta:
        abstract = True
