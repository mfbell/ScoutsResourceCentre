from base import Resource


class Event(Resource)
    plan
    resources
    equipment
    risk_assessment
    location
    leaders
    young_leaders
    young_people
    young_people_approx
    size
    inside_outside

    class Meta:
        abstract = True


class Activity(Event):
    activity_category
    activity
    badges
    badge_requirements
    cost_per_young_person
    cost_approx
    permits
    time_length

    @property
    def total_cost(self):
        return self.cost_per_young_person * self.young_people


class Meeting(Event):
    activities
    extra_costs_per_young_person
    extra_time

    @property
    def total_extra_costs(self):
        return self.extra_costs_per_young_person * self.young_people

    @property
    def total_cost(self):
        return self.total_extra_costs + activities cost

    @property
    def time_length(self):
        return extra_time + activities time_length


class Camp(Event):
    activities
    nights
    days
    start_time
    end_time
    site_cost_per_night_per_young_person
    food_cost_per_day_per_young_person
    other_costs_per_young_person

    @property
    def total_site_cost(self):
        return self.site_cost_per_night_per_young_person * self.young_people * self.nights

    @property
    def total_food_cost(self):
        return self.food_cost_per_day_per_young_person * self.young_people * self.days

    @property
    def total_other_costs(self):
        return self.other_costs_per_young_person * self.young_people

    @property
    def total_cost(self):
        return self.total_site_cost + total_food_cost + total_other_costs + activity costs


class Programme(Resource):
    meetings
    camps
