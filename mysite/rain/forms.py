from django.contrib.gis import forms
from .models import Observatory, PrecipitationMeasurement
from mapwidgets.widgets import GooglePointFieldWidget


class CreateObservatoryForm(forms.ModelForm):
    class Meta(object):
        model = Observatory
        exclude = ['user', 'creation_date']
        widgets = {'location': GooglePointFieldWidget}


class PrecipitationObservationForm(forms.ModelForm):
    class Meta(object):
        model = PrecipitationMeasurement
        fields = ['observatory']
