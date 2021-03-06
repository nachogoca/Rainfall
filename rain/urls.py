from django.conf.urls import url
from . import views as rviews

urlpatterns = [
    url(r'^create$', rviews.create_observatory, name='rain.views.create_observatory'),
    url(r'^upload$', rviews.upload, name='rain.views.upload'),
    url(r'^download$', rviews.download, name='rain.views.download'),
    url(r'^rainfall$', rviews.view_rainfall,  name='rain.views.view_rainfall'),
    url(r'$', rviews.view_observatories, name="rain.views.view_observatories"),
]