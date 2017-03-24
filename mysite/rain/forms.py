from django.contrib.gis import forms
from django.contrib.gis.geos import Point
from .models import Observatory


class CreateObservatoryForm(forms.ModelForm):

    longitude = forms.DecimalField(
        min_value=-180,
        max_value=180,
        required=True,
    )
    latitude = forms.DecimalField(
        min_value=-90,
        max_value=90,
        required=True,
    )


    class Meta(object):
        model = Observatory
        exclude = ['user', 'creation_date']
        # widgets = {'location': forms.OSMWidget(attrs={'map_width': 800})}
        widgets = {'location' : forms.OpenLayersWidget()}

    def __init__(self, *args, **kwargs):
        if args:    # If args exist
            data = args[0]
            if data['latitude'] and data['longitude']:    #If lat/lng exist
                latitude = float(data['latitude'])
                longitude = float(data['longitude'])
                data['location'] = Point(longitude, latitude)    # Set PointField
        try:
            coordinates = kwargs['instance'].point.tuple    #If PointField exists
            initial = kwargs.get('initial', {})
            initial['latitude'] = coordinates[0]    #Set Latitude from coordinates
            initial['longitude'] = coordinates[1]    #Set Longitude from coordinates
            kwargs['initial'] = initial
        except (KeyError, AttributeError):
            pass
        super().__init__(*args, **kwargs)


# class CreateObservatoryForm(forms.ModelForm):

 #    location = forms.PointField(widget=forms.OSMWidget(), required=False, srid=4326)

  #   class Meta:
   #      model = Observatory
    #     fields = ['name', 'about', 'location']
