import json

class AirQualityForecast:
    def __init__(self, file):
        self.file = file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            return json.load(file)

    def save_data_to_file(self):
        with open(self.file, mode="w") as file:
            json.dump(self.data, file)

    def get_weather_data(self, city, date):
        return self.data.get(city, {}).get(date)

    def save_weather_data(self, city, date, weather_info):
        if city not in self.data:
            self.data[city] = {}
        self.data[city][date] = weather_info
        self.save_data_to_file()

    def __setitem__(self, key, value):
        city, date = key
        if city not in self.data:
            self.data[city] = {}
        self.data[city][date] = value

    def __getitem__(self, item):
        city, date = item
        return self.data.get(city, {}).get(date)
