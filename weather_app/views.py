from django.db import IntegrityError
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from .utils import accuweather_handling as awh

# Create your views here.
from weather_app.models import Place
from .forms import FormPlace

API_KEY = "wjIvZkV4FmGKFoW6Zi1BrJzbyufPurjO"


# TODO: ask user for API key?
# TODO: design


# VIEWS
def index(request):
    return render(
        request, 'index.html', {
            'places': nav_sidebar_list(),
            'form': nav_sidebar_form(request),
        }
    )


def place_data(request, _id):
    try:
        place_id = Place.objects.get(pk=_id)

        place_key = awh.get_key(API_KEY, place_id.place_name)

        data_current = get_data_current(place_key)
        data_daily = get_data_daily(place_key)
        data_hourly = get_data_hourly(place_key)

        return render(
            request, 'place.html', {
                'place': place_id,
                'places': nav_sidebar_list(),
                'form': nav_sidebar_form(request),

                'data_current': data_current,
                'data_daily': data_daily,
                'data_hourly': data_hourly,
            })
    except:
        raise Http404("Place doesn't exist in the database")


def place_delete(request, _id):
    place = Place.objects.get(pk=_id)
    print(request.method)
    if request.method == 'POST':
        try:
            place.delete()
            return HttpResponseRedirect(reverse('weather_app:index'))
        except:
            raise Http404("Place doesn't exist in the database")
    else:
        return render(request, 'delete.html', {'place': place})


class PlaceDeleteView(DeleteView):
    model = Place
    template_name = 'delete.html'
    success_url = reverse_lazy('weather_app:delete')


# FUNCTIONS
def nav_sidebar_list():
    return Place.objects.all()


def nav_sidebar_form(request):
    form = FormPlace

    if request.method == 'POST':
        form = FormPlace(request.POST)
        print("POSTING MOMENT")
        print(form.is_valid())
        if form.is_valid():
            post_place(form, Place())

    return form


def post_place(form, place):
    place.place_name = form.cleaned_data['place_name']
    place.place_key = awh.get_key(API_KEY, form.cleaned_data['place_name'])
    try:
        print(place.place_key)
        place.save()
    except IntegrityError as e:
        print(f"Posting result: {place.place_name} ({place.place_key}) | {e}")


def get_data_current(place_key):
    current_data = awh.current(API_KEY, place_key, True).response()
    # hourly_data = awh.hourly(API_KEY, place_key, True).response()
    print(awh.crt_icon(current_data))

    return {
        'crt_temp': awh.crt_temp(current_data),
        'crt_max': awh.crt_max(current_data),
        'crt_min': awh.crt_min(current_data),
        'crt_text': awh.crt_text(current_data),
        'crt_icon': awh.crt_icon(current_data),

        'det_pressure': awh.det_pressure(current_data),
        'det_humidity': awh.det_humidity(current_data),
        'det_clouds': awh.det_clouds(current_data),
        'det_visibility': awh.det_visibility(current_data),

        'wind_dir': awh.wind_dir(current_data),
        'wind_speed': awh.wind_speed(current_data)
    }
    pass


def get_data_daily(place_key):
    daily_data = awh.daily(API_KEY, place_key, True).response()
    daily_array = []
    for i in range(5):
        daily_array.append({
            'day_date': awh.day_date(daily_data, i),
            'day_max': awh.day_max(daily_data, i),
            'day_min': awh.day_min(daily_data, i),
            'day_icon': awh.day_icon(daily_data, i)
        })

    return daily_array


def get_data_hourly(place_key):
    hourly_data = awh.hourly(API_KEY, place_key, True).response()
    hrly_array = []
    for i in range(12):
        hrly_array.append({
            'hrs_temp': awh.hrs_temp(hourly_data, i),
            'hrs_time': awh.hrs_time(hourly_data, i),
            'hrs_icon': awh.hrs_icon(hourly_data, i)
        })

    return hrly_array


def dummy_items():
    dummies = []
    for i in range(15):
        dummies.append(i)
    return dummies
