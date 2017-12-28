from uuid import uuid4

from django.db import models


class Base(models.Model):
    """Base model."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    title = models.CharField(
        max_length=128,
        help_text="Title, not html."
    )
    beavers = models.BooleanField(
        default=False,
    )
    cubs = models.BooleanField(
        default=False,
    )
    scouts = models.BooleanField(
        default=True,
    )
    explorers = models.BooleanField(
        default=False,
    )
    network = models.BooleanField(
        default=False,
    )
    updated = models.DateTimeField(
        auto_now=True,
        help_text="Date-time updated.",
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Requirement(Base):
    """Badge requirement"""
    requirement = models.TextField(
        help_text="The requirement, can be html."
    )


class StagedBadgeCollection(Base):
    """Staged badge collection."""
    desciption = models.TextField(
        blank=True,
        help_text="Staged badge collection description, can be html."
    )


class Badge(Base):
    """Base badge"""
    desciption = models.TextField(
        blank=True,
        help_text="Badge description, can be html."
    )
    CORE = "CO"
    AWARDS = "AW"
    CHALLENGE = "CH"
    ACTIVITY = "AC"
    STAGED = "ST"
    YOUNG_LEADER = "YL"
    CATEGORY = (
        (CORE, "Core Badge"),
        (AWARDS, "Awards"),
        (CHALLENGE, "Challenge Awards"),
        (ACTIVITY, "Activity Badges"),
        (STAGED, "Staged Badges"),
        (YOUNG_LEADER, "Young Leader Award")
    )
    """
    image = models.ImageField(

    )
    """
    categoty = models.CharField(
        max_length=2,
        choices=CATEGORY,
        default=CHALLENGE,
        help_text="Badge type.",
    )
    url = models.URLField(help_text="Link to the badge's page on members.scouts.org.uk.")
    requirements = models.ManyToManyField(
        Requirement,
        help_text="Badge requirements.",
        related_name="badges",
        related_query_name="badge",
    )
    required_badges = models.ManyToManyField(
        "self",
        help_text="Required badges",
        related_name="badges_towards",
        blank=True
    )
    notes = models.TextField(
        blank=True,
        help_text="Exta infomation, can be html."
    )
    guidance_for_leaders = models.TextField(
        blank=True,
        help_text="Guidance for Leaders, can be html."
    )
    """
    activities = models.ManyToManyField(
        activities.activity,
        help_text="Related activities.",
        related_name="badges",
        related_query_name="badge",
    )
    """
    """
    # Stage badges
    stage_towards = models.ForeignKey(
        StagedBadgeCollection,
        help_text="Staged badge collection, only for staged badges.",
        related_name="stages",
        related_query_name="stage",
        blank=True,
    )
    """
