from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CreateObservatoryForm, PrecipitationObservationForm
from .models import Observatory


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
    observatories = Observatory.objects.filter(user=request.user.id)
    return render(request, 'upload.html', {'observatories': observatories})
