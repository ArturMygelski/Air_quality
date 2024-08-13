import requests

def get_air_quality_data(station_id):
    url = f"https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{station_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def get_station_data(city):
    # Wyszukaj stacje w danym mieście
    url = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
    response = requests.get(url)
    if response.status_code == 200:
        stations = response.json()
        city_stations = [station for station in stations if station['city']['name'] == city]
        return city_stations
    else:
        return None

def get_forecast_data(pollutant, teryt_code):
    url = f"https://api.prognozy.ios.edu.pl/v1/{pollutant}/{teryt_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def get_pollutant_data(pollutant, teryt_code):
    url = f"https://api.prognozy.ios.edu.pl/v1/{pollutant}/{teryt_code}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_air_quality_index(pollutant_levels):
    # Mapowanie poziomów stężenia na kategorie jakości powietrza
    quality_categories = {
        "Bardzo dobry": (0, 50),
        "Dobry": (51, 100),
        "Umiarkowany": (101, 150),
        "Zły": (151, 200),
        "Bardzo zły": (201, float('inf'))
    }

    min_level = min(pollutant_levels)

    for category, (low, high) in quality_categories.items():
        if low <= min_level <= high:
            return category

    return "Nieznany"

    # # url = (
    #     # sprwdzenie wszystkich stacji
    #     f"https://api.gios.gov.pl/pjp-api/rest/station/findAll"
    #     # sprwadzenie konkretnej stacji - zapis station_id.json
    #     f"https://api.gios.gov.pl/pjp-api/rest/station/sensors/{stationId}"
    #     # dane pomiarowe - zapis basic_parameter_id.json
    #     f"https://api.gios.gov.pl/pjp-api/rest/data/getData/{sensorId}"
    #     # indeks jakosci powietrza zapis detailed_data.json
    #     f"https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{stationId}"
    #     f"timezone=Europe%2FLondon&start_date={date}&end_date={date}"
    #     # )
