from django.forms import ModelForm, inlineformset_factory

from . import models


class ActivityForm(ModelForm):
    class Meta:
        model = models.Activity
        fields = [
            "title",
            "description",
            "beavers",
            "cubs",
            "scouts",
            "explorers",
            "network",
            "curated",
            "complete",
            "leaders",
            "young_leaders",
            "location",
            "young_people_low",
            "young_people_high",
            "activity_size",
            "inside_outside"
        ]


class ActivityStageForm(ModelForm):
    class Meta:
        model = models.ActivityStage
        fields = [
            "title",
            "description",
            "equipment",
            "risks"
        ]


ActivityStageInlineFormSet = inlineformset_factory(
    models.Activity,
    models.ActivityStage,
    form=ActivityStageForm,
    min_num=1,
    extra=0
)
