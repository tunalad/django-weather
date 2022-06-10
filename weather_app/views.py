from django.http import HttpResponse, Http404
from django.shortcuts import render
from .utils import accuweather_handling as awh

# Create your views here.
from weather_app.models import Place

API_KEY = "8FPhfrAB4eSqEUqWGxOccCRWPFbqDePu"

def index(request):
    return render(request, 'index.html')


def nav_places(request):
    p = Place.objects.all()
    dumms = dummy_items()
    place_key = awh.get_key(API_KEY, "Belgrade")

    return render(request, 'index.html', {'places': p,
                                          'dummies': dumms,
                                          'place_key': place_key})


def dummy_items():
    dummies = []
    for i in range(15):
        dummies.append(i)
    return dummies
