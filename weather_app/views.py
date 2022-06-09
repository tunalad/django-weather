from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from weather_app.models import Place


def index(request):
    return render(request, 'index.html')


def nav_places(request):
    p = Place.objects.all()
    dumms = dummy_items()
    return render(request, 'index.html', {'places': p, 'dummies': dumms})


def dummy_items():
    dummies = []
    for i in range(15):
        dummies.append(i)
    return dummies
