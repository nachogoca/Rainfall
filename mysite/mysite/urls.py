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
from mysite.views import hello, current_datetime, hours_ahead, view_home, view_observatories, view_rainfall, view_download, view_project
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^upload/', include('login.urls')),
    url(r'^hello/$', hello, name='mysite.views.hello'),
    url(r'^$', view_home, name='mysite.views.view_home'),
    url(r'^project/$', view_project, name='mysite.views.view_project'),
    url(r'^observatories/$', view_observatories, name='mysite.views.view_observatories'),
    url(r'^rainfall/$', view_rainfall, name='mysite.views.view_rainfall'),
    url(r'^download/$', view_download, name='mysite.views.view_download'),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
]
