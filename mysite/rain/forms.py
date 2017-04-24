from django.contrib.gis import forms
from .models import Observatory, PrecipitationMeasurement, File
from mapwidgets.widgets import GooglePointFieldWidget
import django_filters


class CreateObservatoryForm(forms.ModelForm):
    class Meta(object):
        model = Observatory
        exclude = ['user', 'creation_date']
        widgets = {'location': GooglePointFieldWidget}


# For dropdown menu in upload page
class OnlyUserObservatoryForm(forms.ModelForm):
    class Meta(object):
        model = PrecipitationMeasurement
        fields = ['observatory']

    def __init__(self, form=None, user=None, **kwargs):
        super(OnlyUserObservatoryForm, self).__init__(form, **kwargs)
        if user:
            self.fields['observatory'].queryset = Observatory.objects.filter(user=user)


class DownloadForm(forms.ModelForm):
    choices = [[x.id, x] for x in Observatory.objects.all()]
    observatory_choices = forms.MultipleChoiceField(choices=choices)

    class Meta(object):
        model = Observatory
        fields = []

class ObservationForm(forms.ModelForm):
    class Meta(object):
        model = PrecipitationMeasurement
        exclude = []


class UploadForm(forms.Form):
    class Meta(object):
        model = File
