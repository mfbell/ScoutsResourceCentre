"""ResourceCentre models."""

import uuid

from django.conf import settings
from django.db import models


PK = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class ResourceSlug(models.Model):
    """Resource slug handling model."""
    id = PK
    slug = models.SlugField(
        unique=True,
        help_text="Custom resource URL."
    )

class Resource(models.Model):
    """Base resource model."""
    id = PK
    title = models.CharField(max_length=128)
    slug = models.OneToOneField(
        ResourceSlug,
        on_delete=models.CASCADE,
        related_name="resource"
    )
    description = models.CharField(max_length=512, blank=True)
    beavers = models.BooleanField(default=False)
    cubs = models.BooleanField(default=False)
    scouts = models.BooleanField(default=True)
    explorers = models.BooleanField(default=False)
    network = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    curated = models.BooleanField(default=False)
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        help_text="Users who have contributed to the resource.",
        blank=True
    )
    complete = models.BooleanField(
        default=False,
        help_text="Finished resource."
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class RiskAssessmentRisk(models.Model):
    """Risk Assessment Risk model."""
    id = PK
    risk = models.CharField(
        max_length=128,
        help_text="State the risk.",
    )
    cause = models.CharField(
        max_length=256,
        help_text="State the cause.",
    )
    LEADERS = "LE"
    YOUNG_PEOPLE = "YP"
    EVERYONE = "EV"
    AFFECTEES = (
        (LEADERS, "Leaders"),
        (YOUNG_PEOPLE, "Young people"),
        (EVERYONE, "Everyone"),
    )
    affectee = models.CharField(
        max_length=2,
        choices=AFFECTEES,
        default=EVERYONE,
        help_text="Who is at risk.",
    )
    NEGLIGIBLE = "NE"
    LOW = "LO"
    MEDIUM = "ME"
    HIGH = "HI"
    RATINGS = (
        (NEGLIGIBLE, "Negligible"),
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    )
    severity = models.CharField(
        max_length=2,
        choices=RATINGS,
        default=MEDIUM,
        help_text="The severity of the risk.",
    )
    chance = models.CharField(
        max_length=2,
        choices=RATINGS,
        default=LOW,
        help_text="The chance of happening.",
    )
    mitigation = models.CharField(
        max_length=256,
        help_text="How will you reduce the risk?",
    )
    responce = models.CharField(
        max_length=256,
        help_text="How to respond to an incident.",
    )

    @property
    def level(self):
        """Risk level calculator."""
        severity = self.RATINGS.index(self.severity) + 1
        chance = self.RATINGS.index(self.chance) + 1
        risk = severity * chance
        if risk < 4:
            return "Low"
        elif risk < 8:
            return "Medium"
        elif risk < 12:
            return "High"
        else:
            return "Extream"


class RiskAssessment(Resource):
    """Risk Assessment model."""
    risks = models.ManyToManyField(RiskAssessmentRisk)


class Activity(Resource):
    """Activity model."""
    leaders = models.IntegerField(
        default=3,
        help_text="Number of leaders needed.",
    )
    young_leaders = models.IntegerField(
        default=0,
        help_text="Number of young leaders.",
    )
    location = models.CharField(
        max_length=256,
        help_text="Event location.",
    )
    young_people_low = models.IntegerField(help_text="Minimum number of young people.")
    young_people_high = models.IntegerField(help_text="Maximum number of young people.")
    INDIVIDUAL = "ID"
    PATROL = "PA"
    TROOP = "TR"
    DISTRICT = "DI"
    COUNTY = "CO"
    NATIONAL = "NA"
    INTERNATIONAL = "IN"
    SIZIES = (
        (INDIVIDUAL, "Individual"),
        (PATROL, "Patrol"),
        (TROOP, "Troop"),
        (DISTRICT, "District"),
        (COUNTY, "County"),
        (NATIONAL, "National"),
        (INTERNATIONAL, "International"),
    )
    activity_size = models.CharField(
        max_length=2,
        choices=SIZIES,
        default=TROOP,
        help_text="Activity size.",
    )
    INSIDE = "IN"
    OUTSIDE = "OU"
    BOTH = "BO"
    EITHER = "EI"
    SIDES = (
        (OUTSIDE, "Outside only"),
        (INSIDE, "Inside only"),
        (EITHER, "Inside or outside"),
        (BOTH, "Inside and outside"),
    )
    inside_outside = models.CharField(
        max_length=2,
        choices=SIDES,
        default=OUTSIDE,
        help_text="Is the event inside, outside or both.",
    )


class ActivityStage(models.Model):
    id = PK
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(help_text="Stage explanation.")
    equipment  = models.TextField(blank=True)
    risks = models.ManyToManyField(RiskAssessmentRisk)


def uuid4_filename(instance, filename):
    ext = filename.split()[-1]
    name = uuid.uuid4().hex
    return "{}.{}".format(name, ext)

class ActivityStageImage(models.Model):
    id = PK
    activity_stage = models.ForeignKey(ActivityStage, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=uuid4_filename)
    description = models.CharField(max_length=128, blank=True)
