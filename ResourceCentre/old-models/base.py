"""Base models."""

# PK
import uuid
# external_id
import string
import random
# auto_slug
import re

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


def get_sentinel_user():
    """Get sentinel user."""
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Resource(models.Model):
    """Base resource"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(
        max_length=128,
        help_text="A short, one-point title for your resources.",
    )
    slug = models.SlugField(
        # max_length default 50
        help_text="Keep it short but specific."
    )
    desciption = models.CharField(
        max_length=512,
        blank=True,
        help_text="Summerise  your resources.",
    )
    beavers = models.BooleanField(
        default=False,
        help_text="Aimed at the Beaver section.",
    )
    cubs = models.BooleanField(
        default=False,
        help_text="Aimed at the Cub section.",
    )
    scouts = models.BooleanField(
        default=True,
        help_text="Aimed at the Scout section.",
    )
    explorers = models.BooleanField(
        default=False,
        help_text="Aimed at the Explorer section.",
    )
    network = models.BooleanField(
        default=False,
        help_text="Aimed at the Beavers section.",
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
        help_text="Curated resource.",
    )
    # Inherited FK related name/query name catch
    # https://docs.djangoproject.com/en/1.11/topics/db/models/#be-careful-with-related-name-and-related-query-name
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        editable=False,
        help_text="The orginal creator.",
        related_name="%(class)s_created_resources",
        related_query_name="%(class)s_created_resource",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        help_text="The resource owner.",
        related_name="%(class)s_owned_resources",
        related_query_name="%(class)s_owned_resource",
    )
    editors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        help_text="Users with permission to edit the resource.",
        related_name="%(class)s_editor_roles",
        related_query_name="%(class)s_editor_role",
        blank=True
    )
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        help_text="Users who have contributed to the resource.",
        related_name="%(class)s_contributions",
        related_query_name="%(class)s_contribution",
        blank=True
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
        null=True,
        blank=True,
        on_delete=models.SET(get_sentinel_parent),
        help_text="For if the resource was a copy and edited, the parent.",
        related_name="%(class)s_children",
        related_query_name="%(class)s_child",
    )
    # View to move to another table.
    views = models.IntegerField(default=0)
    #generated_from <- future feature

    # Regex whole word slug shortener
    _re_slug_shortener = re.compile(r"^([\w-]{0, %d})-" % slug.max_length)

    def auto_slugify(self):
        """Set slug from title."""
        self.slug = self.slugify(self.title)

    def slugify(self, text):
        """Generate whole word slug no longer than slug.max_length."""
        slug = slugify(text)
        if len(slug) > self.slug.max_length:
            match = self._re_slug_shortener(slug)
            slug = match.group(1)
        return slug

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
        return ": ".join([self.__doc___, self.title])

    class Meta:
        abstract = True
