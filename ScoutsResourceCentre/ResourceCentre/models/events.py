"""Event models."""

from datetime import time

from .base import Resource
from .riskAssessment import RiskAssessment


def default_camp_start_time():
    """Returns datetime time object set to 19:00."""
    return time(19, 0)

def defaut_camp_end_time():
    """Returns datetime time object set to 16:00."""
    return time(16, 0)


class Event(Resource):
    """Base event model."""
    plan = models.TextField(help_text="The event plan.")
    resources = models.TextField(help_text="Resources needed to run the event.")
    equipment  = models.TextField(help_text="Equipment needed to run the event.")
    risk_assessment  = models.ForeignKey(
        RiskAssessment,
        on_delete=models.PROTECT,
        help_text="Event risk assessment."
    )
    location = models.CharField(
        max_length=256,
        help_text="Event location.",
    )
    # Could at location database.
    leaders = models.IntegerField(help_text="Number of leaders needed.")
    young_leaders = models.IntegerField(help_text="Number of young leaders.")
    young_people = models.IntegerField(help_text="Number of young people.")
    young_people_approx = models.BooleanField(
        default=False,
        help_text="Is the number of young people an approximate number?",
    )
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
    size = models.CharField(
        max_length=2,
        choices=SIZIES,
        default=TROOP,
        help_text="Event size.",
    )
    INSIDE = "IN"
    OUTSIDE = "OU"
    BOTH = "BO"
    EITHER = "EI"
    SIDES = (
        (INSIDE, "Inside only"),
        (OUTSIDE, "Outside only"),
        (EITHER, "Inside or outside"),
        (BOTH, "Inside and outside"),
    )
    inside_outside = models.CharField(
        max_length=2,
        choices=SIDES,
        default=EITHER,
        help_text="Is the event inside, outside or both.",
    )

    def __str__(self):
        return "Base event model"

    class Meta:
        abstract = True


class Activity(Event):
    """Activity model."""
    PLACEHOLDER = "PL"
    PLACEHOLDERS = (
        (PLACEHOLDER, "Placeholder 1"),
        (PLACEHOLDER, "Placeholder 2"),
    )
    activity_category = models.CharField(
        max_length=2,
        choices=PLACEHOLDERS,
        help_text="Is the activity inside, outside or both.",
    )
    activity = models.CharField(
        max_length=2,
        choices=PLACEHOLDERS,
        help_text="Is the activity inside, outside or both.",
    )
    # Should make activties/cats a table
    badges = models.ManyToManyField(
        'BadgeManager.Badges',
        on_delete=models.PROTECT,
        help_text="Badges related to the activity.",
    )
    badge_requirements = models.ManyToManyField(
        'BadgeManager.Requirements',
        on_delete=models.PROTECT,
        help_text="Badge requirements related to the activity.",
    )
    cost_per_young_person = models.DecimalField(
        max_digits=11
        decimal_places=2
        help_text="Cost per young person."
    )
    cost_approx = models.BooleanField(
        default=False,
        help_text="Is the cost per young person an approximate number?",
    )
    #permits permits should be under activities.
    time_length = models.DurationField(help_text="Activity length.")

    @property
    def total_cost(self):
        """Total cost calculator."""
        return self.cost_per_young_person * self.young_people

    def __str__(self):
        return "Activity"


class Meeting(Event):
    """Meeting model."""
    activities = models.ManyToManyField(
        Activity,
        on_delete=models.PROTECT,
        help_text="Activities happening at the meeting.",
    )
    extra_costs_per_young_person = models.DecimalField(
        max_digits=11
        decimal_places=2
        help_text="Extra meeting costs per young person."
    )
    extra_cost_approx = models.BooleanField(
        default=False,
        help_text="Is the extra costs per young person an approximate number?",
    )
    extra_time = models.DurationField(help_text="Extra time needed for the meeting.")

    @property
    def total_extra_costs(self):
        """Total extra costs calculator."""
        return self.extra_costs_per_young_person * self.young_people

    @property
    def total_cost(self):
        """Total cost calculator."""
        return self.total_extra_costs + activities cost

    @property
    def time_length(self):
        """Total time calculator."""
        return extra_time + activities time_length

    def __str__(self):
        return "Meeting"


class Camp(Event):
    """Camp model."""
    activities = models.ManyToManyField(
        Activity,
        on_delete=models.PROTECT,
        help_text="Activities happening at the meeting.",
    )
    nights = models.IntegerField(help_text="Number of nights")
    start_time = models.TimeField(
        default=default_camp_start_time
        help_text="Camp start time."
    )
    end_time = models.TimeField(
        default=default_camp_end_time
        help_text="Camp end time."
    )
    site_cost_per_young_person_per_night = models.DecimalField(
        max_digits=11
        decimal_places=2
        help_text="Site costs per young person per nights."
    )
    food_cost_per_young_person_per_day = models.DecimalField(
        max_digits=11
        decimal_places=2
        help_text="Food costs per young person per day."
    )
    other_costs_per_young_person = models.DecimalField(
        max_digits=11
        decimal_places=2
        help_text="Extra camp costs per young person."
    )

    @property
    def total_site_cost(self):
        """Total site cost calculator."""
        return self.site_cost_per_night_per_young_person * self.young_people * self.nights

    @property
    def total_food_cost(self):
        """"Total food cost calculator."""
        return self.food_cost_per_day_per_young_person * self.young_people * self.nights

    @property
    def total_other_costs(self):
        """Total other costs calculator."""
        return self.other_costs_per_young_person * self.young_people

    @property
    def total_cost(self):
        """Total cost calculator."""
        return self.total_site_cost + total_food_cost + total_other_costs + activity costs

    def __str__(self):
        return "Camp"


"""Future resource.
class Programme(Resource):
    meetings
    camps
"""
