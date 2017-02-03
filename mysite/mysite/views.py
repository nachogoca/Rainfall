from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hours(s), it will be %s." % (offset, dt)
    return HttpResponse(html)

def home(request):
    return render(request, 'navbar.html')
    
