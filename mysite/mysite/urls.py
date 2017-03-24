"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from mysite.views import *
from rain import views as rain_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', view_home, name='mysite.views.view_home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name':'login.html', 'redirect_field_name':'mysite.views.view_home'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^register/$', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/login/'
    ), name='register'),
    url(r'^upload/', view_upload, name='mysite.views.view_upload'),
    url(r'^project/$', view_project, name='mysite.views.view_project'),
    url(r'^observatories/create$', rain_views.create_observatory, name='rain.views.create_observatory'),
    url(r'^observatories/', view_observatories, name='mysite.views.view_observatories'),
    url(r'^rainfall/$', view_rainfall, name='mysite.views.view_rainfall'),
    url(r'^download/$', view_download, name='mysite.views.view_download'),
]
