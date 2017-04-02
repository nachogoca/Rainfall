import csv
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CreateObservatoryForm, UploadForm, ObservationForm, OnlyUserObservatoryForm
from .models import Observatory, File


@login_required(login_url='/login/')
def create_observatory(request):
    if request.method == "POST":
        form = CreateObservatoryForm(request.POST)

        if form.is_valid():
            obs = form.save(commit=False)
            obs.creation_date = timezone.now()
            obs.user_id = request.user.id
            obs.save()
            return redirect('rain.views.view_observatories')
    else:
        form = CreateObservatoryForm()
    return render(request, 'create_observatory.html', {'form':form})


def view_observatories(request):
    observatories = Observatory.objects.all()
    return render(request, 'observatories.html', {'observatories': observatories})


@login_required(login_url='/login/')
def upload(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['csv_file']
        observatories_form = OnlyUserObservatoryForm(form=request.POST, user=request.user.id)
        if observatories_form.is_valid():
            obs_id = observatories_form.cleaned_data['observatory'].id
        else:
            return redirect('rain.views.upload')

        for line in file:

            data = {'observatory': obs_id,
                    'rainfall_rate': 1.32,
                    'precipitation_24hr': 45.2}
            obs_form = ObservationForm(data=data)
            obs = obs_form.save(commit=False)
            print("to be saved")
            print(obs.observatory)
            print(obs.rainfall_rate)
            print(obs.precipitation_24hr)

        return redirect('rain.views.view_observatories')
    else:
        observatories_form = OnlyUserObservatoryForm(user=request.user.id)
    return render(request, 'upload.html', {'observatories_form': observatories_form})


@login_required(login_url='/login/')
def upload_success(request):
    return render(request, 'project.html') # TODO Create success page
