from django.contrib.gis import forms
from .models import Observatory
from mapwidgets.widgets import GooglePointFieldWidget


class CreateObservatoryForm(forms.ModelForm):
    class Meta(object):
        model = Observatory
        exclude = ['user', 'creation_date']
        widgets = {'location': GooglePointFieldWidget}
