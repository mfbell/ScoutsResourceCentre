from django.contrib import admin

from . import models


admin.site.register(models.Requirement)
admin.site.register(models.Badge)
admin.site.register(models.StagedBadgeCollection)
