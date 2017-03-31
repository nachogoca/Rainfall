from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def view_home(request):
    return render(request, 'home.html')


def view_project(request):
    return render(request, 'project.html')


# def view_observatories(request):
#     return render(request, 'observatories.html')


def view_rainfall(request):
    return render(request, 'rainfall.html')


def view_download(request):
    return render(request, 'download.html')


@login_required(login_url='/login/')
def view_upload(request):
    return render(request, 'upload.html')

