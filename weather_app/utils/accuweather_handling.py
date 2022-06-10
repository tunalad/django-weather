import requests


def get_data(api_key, place):  # {{{
    """ returns json data of a place """
    return requests.get(
        "https://dataservice.accuweather.com/locations/v1/cities/search?apikey="
        + api_key + "&q=" + place)  # }}}


def get_key(api_key, place):  # {{{
    """ returns a key of the place """
    place_data = requests.get("https://dataservice.accuweather.com/locations/v1/cities/search?apikey="
                              + api_key + "&q=" + place)
    # place_key = place_data.json()[0]["Key"]
    print("https://dataservice.accuweather.com/locations/v1/cities/search?apikey=" +
          api_key + "&q=" + place)
    try:
        return place_data.json()[0]["Key"]
    except:
        return "Place doesn't exist"  # }}}


class current:  # {{{
    def __init__(self, api_key, place_key, metric):
        self.api_key = api_key
        self.place_key = place_key
        self.metric = metric

    def response(self):
        """ returns json data for the current conditions """
        return requests.get(
            "https://dataservice.accuweather.com/currentconditions/v1/" +
            self.place_key + "?apikey=" +
            self.api_key + "&details=true&metric=" + str(self.metric).lower())
        # }}}


class hourly:  # {{{
    def __init__(self, api_key, place_key, metric):
        self.api_key = api_key
        self.place_key = place_key
        self.metric = metric

    def response(self):
        """ returns json data for the hourly forecast """
        return requests.get("https://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" +
                            self.place_key + "?apikey=" +
                            self.api_key + "&details=true&metric=" + str(self.metric).lower())
        # }}}


class daily:  # {{{
    def __init__(self, api_key, place_key, metric):
        self.api_key = api_key
        self.place_key = place_key
        self.metric = metric

    def response(self):
        """ returns json data for the daily forecast """
        return requests.get("https://dataservice.accuweather.com/forecasts/v1/daily/5day/" +
                            self.place_key + "?apikey=" +
                            self.api_key + "&details=true&metric=" + str(self.metric).lower())  # }}}


def crt_temp(item_current):
    return item_current.json()[0]["Temperature"]["Metric"]["Value"]


def crt_max(item_current):
    return item_current.json()[0]["TemperatureSummary"]["Past6HourRange"]["Maximum"]["Metric"]["Value"]


def crt_min(item_current):
    return item_current.json()[0]["TemperatureSummary"]["Past6HourRange"]["Minimum"]["Metric"]["Value"]


def crt_text(item_current):
    return item_current.json()[0]["WeatherText"]


def hrs_temp(item_hourly, i):
    return item_hourly.json()[int(i)]["Temperature"]["Value"]


def hrs_time(item_hourly, i):
    return str(item_hourly.json()[int(i)]["DateTime"])[11:-9]


def hrs_icon(item_hourly, i):
    return str(item_hourly.json()[int(i)]["WeatherIcon"])


def day_date(item_daily, i):
    return str(item_daily.json()["DailyForecasts"][i]["Date"])[:-15]


def day_max(item_daily, i):
    return item_daily.json()["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]


def day_min(item_daily, i):
    return item_daily.json()["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]


def day_icon(item_daily, i):
    return item_daily.json()["DailyForecasts"][i]["Day"]["Icon"]


def det_pressure(item_current):
    return item_current.json()[0]["Pressure"]["Metric"]["Value"]


def det_humidity(item_current):
    return item_current.json()[0]["RelativeHumidity"]


def det_clouds(item_current):
    return item_current.json()[0]["CloudCover"]


def det_visibility(item_current):
    return item_current.json()[0]["Visibility"]["Metric"]["Value"]


def wind_dir(item_current):
    return item_current.json()[0]["Wind"]["Direction"]["Localized"]


def wind_speed(item_current):
    return item_current.json()[0]["Wind"]["Speed"]["Metric"]["Value"]
