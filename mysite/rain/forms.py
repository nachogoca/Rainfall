from django.contrib.gis import forms
from .models import Observatory, PrecipitationMeasurement, File
from mapwidgets.widgets import GooglePointFieldWidget


class CreateObservatoryForm(forms.ModelForm):
    class Meta(object):
        model = Observatory
        exclude = ['user', 'creation_date']
        widgets = {'location': GooglePointFieldWidget}


class OnlyUserObservatoryForm(forms.ModelForm):
    class Meta(object):
        model = PrecipitationMeasurement
        fields = ['observatory']

    def __init__(self, form=None, user=None, **kwargs):
        super(OnlyUserObservatoryForm, self).__init__(form, **kwargs)
        if user:
            self.fields['observatory'].queryset = Observatory.objects.filter(user=user)


class ObservationForm(forms.ModelForm):
    class Meta(object):
        model = PrecipitationMeasurement
        fields = ['observatory', 'precipitation_24hr', 'rainfall_rate']


class UploadForm(forms.Form):
    class Meta(object):
        model = File
