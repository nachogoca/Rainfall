from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateObservatoryForm
# Create your views here.


@login_required(login_url='/login/')
def create_observatory(request):
    if request.method == "POST":
        request.POST._mutable = True
        form = CreateObservatoryForm(request.POST)
        obs = form.save(commit=False)
        print(obs.location)
    else:
        form = CreateObservatoryForm()
    return render(request, 'create_observatory.html', {'form':form})