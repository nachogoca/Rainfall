from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CreateObservatoryForm
# Create your views here.


@login_required(login_url='/login/')
def create_observatory(request):
    if request.method == "POST":
        request.POST._mutable = True
        form = CreateObservatoryForm(request.POST)
        request.POST._mutable = False

        if form.is_valid():
            obs = form.save(commit=False)
            obs.user_id = request.user.id
            print(obs.user_id)
            obs.creation_date = timezone.now()
            print(obs.creation_date)
            print(obs.name)
            print(obs.about)
            print(obs.location)
            obs.save()
    else:
        form = CreateObservatoryForm()
    return render(request, 'create_observatory.html', {'form':form})