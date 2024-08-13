from geopy.geocoders import Nominatim

def get_coordinates(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude