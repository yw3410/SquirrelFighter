from django.shortcuts import render, redirect

from django.http import HttpResponse,HttpResponseRedirect
from sightings.models import squirrels
from .forms import SquirrelForm

def index(request):
    sightings=squirrels.objects.all()
    context={'sightings':sightings,}
    return render(request,"sightings/index.html",context)

def add(request):
    if request.method=="POST":
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings:index')
    else:
        form=SquirrelForm()
    context={'form':form}
    return render(request,'sightings/add.html',context)

def delete(request, Unique_Squirrel_ID):
    sighting=squirrels.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=='POST':
        sighting.delete()
        return redirect('sightings:index')
    else:
        context={'sighting':sighting}
        return(render(request,'sightings/delete.html',context))

def update(request, Unique_Squirrel_ID):
    sighting = squirrels.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        form=SquirrelForm(request.POST,instance=sighting)
        if form.is_valid():
            form.save()
            return redirect('sightings:index')
    else:
        form=SquirrelForm(instance=sighting)
    context={'form':form}
    return render(request,'sightings/update.html',context)

def stats(request):
    all_count = Sighting.objects.all().count()
    black_fur = squirrels.objects.filter(Primary_fur_color='Black').count()
    gray_fur = squirrels.objects.filter(Primary_fur_color='GRAY').count()
    cinnamon_fur = squirrels.objects.filter(Primary_fur_color='CINNAMON').count()
    adult_count = squirrels.objects.filter(age='Adult').count()
    juv_count = squirrels.objects.filter(age='Juvenile').count()
    running = squirrels.objects.filter(Running=True).count()
    not_runing = squirrels.objects.filter(Running=False).count()
    chasing = squirrels.objects.filter(Chasing=True).count()
    climbing = squirrels.objects.filter(Climbing=True).count()
    eating = squirrels.objects.filter(Eating=True).count()
    foraging = squirrels.objects.filter(Foraging=True).count()

    context = {
            'all_count' : all_count,
            'black_fur' : black_fur,
            'gray_fur' : gray_fur,
            'cinnamon_fur' : cinnamon_fur,
            'adult': adult,
            'juvenile': juvenile,
            'running' : running,
            'not_running': not_running,
            'chasing' = chasing,
            'climbing' = climbing,
            'eating' = eating,
            'foraging' = foraging,
            }
    return render(request,'sightings/stats.html',context)

