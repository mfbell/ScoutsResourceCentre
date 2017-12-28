from django.contrib import admin

from .models import events, riskassessments


admin.site.register(events.Activity)
admin.site.register(events.Meeting)
admin.site.register(events.Camp)

admin.site.register(riskassessments.RiskAssessment)
admin.site.register(riskassessments.RiskAssessmentElement)
