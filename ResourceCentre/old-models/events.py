"""Event models."""

from datetime import time, timedelta

from django.db import models

from .base import Resource
from .riskassessments import RiskAssessment


def default_camp_start_time():
    """Returns datetime time object set to 19:00."""
    return time(19)

def default_camp_end_time():
    """Returns datetime time object set to 16:00."""
    return time(16)




class Meeting(Event):
    """Meeting"""
    activities = models.ManyToManyField(
        Activity,
        help_text="Activities happening at the meeting.",
        related_name="meetings",
        related_query_name="meeting",
    )
    extra_costs_per_young_person = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        help_text="Extra meeting costs per young person.",
    )
    extra_cost_approx = models.BooleanField(
        default=False,
        help_text="Is the extra costs per young person an approximate number?",
    )
    extra_duration = models.DurationField(
        help_text="Extra time needed for the meeting.",
    )

    @property
    def total_extra_costs(self):
        """Total extra costs calculator."""
        return self.extra_costs_per_young_person * self.young_people

    @property
    def total_cost(self):
        """Total cost calculator."""
        cost = self.total_extra_costs
        for activity in self.activities.objects.all():
            cost += activity.total_cost
        return cost

    @property
    def time_length(self):
        """Total time calculator."""
        time = self.extra_duration
        for activity in self.activities.objects.all():
            time += activity.duration
        return time


class Camp(Event):
    """Camp"""
    activities = models.ManyToManyField(
        Activity,
        help_text="Activities happening at the camp.",
        related_name="camps",
        related_query_name="camp",
    )
    nights = models.IntegerField(help_text="Number of nights")
    start_time = models.TimeField(
        default=default_camp_start_time,
        help_text="Camp start time.",
    )
    end_time = models.TimeField(
        default=default_camp_end_time,
        help_text="Camp end time.",
    )
    site_cost_per_young_person_per_night = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        help_text="Site costs per young person per nights.",
    )
    food_cost_per_young_person_per_day = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        help_text="Food costs per young person per day.",
    )
    other_costs_per_young_person = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        help_text="Extra camp costs per young person.",
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
        cost = self.total_site_cost + total_food_cost + total_other_costs
        for activity in self.activities.objects.all():
            cost += activity.total_cost
        return cost


"""Future resource.
class Programme(Resource):
    meetings
    camps
"""
