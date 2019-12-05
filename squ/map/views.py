from django.shortcuts import render
from models import squirrels

def squirrels_map(request):
    sightings=squirrels.objects.all()[:100]
    
    return render(request, 'map/squirrels_map.html',{'sightings':sightings})
# Create your views here.
