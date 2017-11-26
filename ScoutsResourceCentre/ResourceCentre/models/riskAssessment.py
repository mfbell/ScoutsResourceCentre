from django.db import models

from base import Resource


class RiskAssessmentElement(Resource):
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
    AFFECTANTS = (
        (LEADERS, "Leaders"),
        (YOUNG_PEOPLE, "Young people"),
        (EVERYONE, "Everyone"),
    )
    affects = models.CharField(
        max_length=2,
        choices=AFFECTANTS,
        default=EVERYONE,
        help_text="Who is at risk.",
    )
    mitigations = models.CharField(
        max_length=256,
        help_text="How will you reduce the risk?",
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
        help_text="The severity of the risk after mitigation.",
    )
    chance = models.CharField(
        max_length=2,
        choices=RATINGS,
        default=LOW,
        help_text="The chance of the risk after mitigation.",
    )
    responce = models.CharField(
        max_length=256,
        help_text="How to respond to an incident.",
    )

    @property
    def level(self):
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
    elements = models.ManyToManyField(
        RiskAssessmentElement,
        on_delete=models.PROTECT,
        help_text="Risk asessments are made up of individual risk assessments for reusability.",
    )

    @property
    def level(self):
        return risk bases on elements' risk level
