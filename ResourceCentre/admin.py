from django.contrib import admin

from .models import Resource, RiskAssessment, RiskAssessmentRisk, Activity, \
ActivityStage, ActivityStageImage


admin.site.register(RiskAssessment)
admin.site.register(RiskAssessmentRisk)
admin.site.register(Activity)
admin.site.register(ActivityStage)
admin.site.register(ActivityStageImage)
