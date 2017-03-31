from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    string = models.CharField(max_length=100)
    point = models.PointField()
    creation_date = models.DateField()

    def __str__(self):
        return "%s %s %s" % (self.string, self.point, self.creation_date)


class Observatory(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200, blank=True)
    location = models.PointField()
    creation_date = models.DateField()

    objects = models.GeoManager()

    def __str__(self):
        return '%s %s %s %s %s' % (self.name, self.user, self.about, self.location, self.creation_date)


class PrecipitationMeasurement(models.Model):
    observatory = models.ForeignKey(Observatory)
    precipitation_24hr = models.FloatField()
    rainfall_rate = models.FloatField()

    def __str__(self):
        return u'%s %s' % (self.precipitation_24hr, self.rainfall_rate)
