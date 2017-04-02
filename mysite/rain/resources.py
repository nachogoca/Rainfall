from .models import PrecipitationMeasurement
from import_export import resources, fields


class UploadPrecipitationResource(resources.ModelResource):
    rainfall_rate = fields.Field(attribute='rainfall_rate',
                                 column_name='Rainfall rate')
    precipitation_24hr = fields.Field(attribute='precipitation_24hr',
                                      column_name='Precipitation 24Hr')

    class Meta(object):
        model = PrecipitationMeasurement
        fields = ('rainfall_rate', 'precipitation_24hr')
        export_order = fields
