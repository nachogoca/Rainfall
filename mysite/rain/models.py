from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Observatory(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200, blank=True)
    creation_date = models.DateField()

    def __str__(self):
        return self.name

class ObservatoryLocation(models.Model):
    observatory = models.ForeignKey(Observatory)
    location = models.PointField(srid=4326)
    about = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.location

class PrecipitationMeasurement(models.Model):
    observatory_location = models.ForeignKey(ObservatoryLocation)
    precipitation_24hr = models.FloatField()
    rainfall_rate = models.FloatField()

    def __str__(self):
        return u'%s %s' % (self.precipitation_24hr, self.rainfall_rate)

