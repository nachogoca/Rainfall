import csv, json
import dateutil.parser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CreateObservatoryForm, UploadForm, ObservationForm, OnlyUserObservatoryForm
from .models import Observatory, PrecipitationMeasurement


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


def view_rainfall(request):
    observatories = Observatory.objects.all()
    last_measurements = []
    for observatory in observatories:
        try:
            last_measurement = PrecipitationMeasurement.objects.filter(observatory=observatory).latest('measure_datetime')
        except PrecipitationMeasurement.DoesNotExist:
            last_measurement = None
        last_measurements.append(last_measurement)

    print(last_measurements)
    return render(request, 'rainfall.html', {'last_measurements':last_measurements})


@login_required(login_url='/login/')
def upload(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['csv_file']
        observatories_form = OnlyUserObservatoryForm(form=request.POST, user=request.user.id)
        if observatories_form.is_valid():
            obs_id = observatories_form.cleaned_data['observatory'].id
        else:
            return redirect('rain.views.upload')

        try:
            json_str = file.read().decode('utf-8')
            json_obj = json.loads(json_str)

            for obs_obj in json_obj:
                data = {'observatory': obs_id,
                        'rainfall_rate': obs_obj['rainfall_rate'],
                        'measure_datetime': dateutil.parser.parse(obs_obj['measure_datetime'])}
                obs_form = ObservationForm(data=data)
                obs_form.save()
        except:
            return render(request, "upload_error.html")
        else:
            return render(request, "upload_success.html")
    else:
        observatories_form = OnlyUserObservatoryForm(user=request.user.id)
    return render(request, 'upload.html', {'observatories_form': observatories_form})


