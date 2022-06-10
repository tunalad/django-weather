from django.http import HttpResponse, Http404
from django.shortcuts import render
from .utils import accuweather_handling as awh

# Create your views here.
from weather_app.models import Place

API_KEY = "f99EIdRXeca8kvZOMOuxKzeApNimk3KE"


def index(request):
    return render(request, 'index.html')


def nav_places(request):
    p = Place.objects.all()
    dumms = dummy_items()

    place_key = awh.get_key(API_KEY, "Belgrade")
    data_current = get_data_current(place_key)
    data_daily = get_data_daily(place_key)
    data_hourly = get_data_hourly(place_key)

    return render(
        request, 'index.html', {
            'places': p,
            'dummies': dumms,
            'data_current': data_current,
            'data_daily': data_daily,
            'data_hourly': data_hourly
        }
    )


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
