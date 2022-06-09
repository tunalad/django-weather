from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from weather_app.models import Place


def index(request):
    return render(request, 'index.html')


def nav_places(request):
    p = Place.objects.all()
    print(p)
    return render(request, 'index.html', {'places': p})
