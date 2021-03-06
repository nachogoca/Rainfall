from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Observatory(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200, blank=True)
    location = models.PointField()
    creation_date = models.DateField()

    objects = models.GeoManager()

    def __str__(self):
        return '%s,\t%s\n' % (self.name, self.about)
        # return '%s\t%s\t%s\t%s\t%s\n' % (self.name, self.user, self.about, self.location, self.creation_date)


class PrecipitationMeasurement(models.Model):
    observatory = models.ForeignKey(Observatory)
    rainfall_rate = models.FloatField()
    measure_datetime = models.DateTimeField()

    def __str__(self):
        return '%s at %s\n' % (self.rainfall_rate, self.measure_datetime)


class File(models.Model):
    docfile = models.FileField(upload_to='upload/%Y/%m/%d')


