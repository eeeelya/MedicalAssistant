from django_filters import DateTimeFromToRangeFilter, FilterSet, filters, widgets

from medcard.models import MedicalCard


class MedCardFilter(FilterSet):
    blood_type = filters.ChoiceFilter(choices=MedicalCard.BloodType.choices)
    created = DateTimeFromToRangeFilter(widget=widgets.RangeWidget(attrs={"type": "date"}))

    # TODO: create more filters

    class Meta:
        model = MedicalCard
        fields = [
            "blood_type",
            "created",
        ]
