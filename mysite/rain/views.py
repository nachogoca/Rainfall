from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CreateObservatoryForm
# from .forms import TestForm
# Create your views here.


@login_required(login_url='/login/')
def create_observatory(request):
    if request.method == "POST":
        form = CreateObservatoryForm(request.POST)

        if form.is_valid():
            obs = form.save(commit=False)
            obs.creation_date = timezone.now()
            obs.user_id = request.user.id
            obs.save()
            return render(request, "observatories.html")
    else:
        form = CreateObservatoryForm()
    return render(request, 'create_observatory.html', {'form':form})