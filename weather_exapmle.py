from weather_data import get_air_quality_data, get_station_data

def main():
    city = input("Podaj miasto: ")
    stations = get_station_data(city)
    if not stations:
        print("Nie znaleziono stacji dla podanego miasta.")
        return

    print("Dostępne stacje:")
    for idx, station in enumerate(stations):
        print(f"{idx + 1}. {station['stationName']} - {station['addressStreet']}")

    station_idx = int(input("Wybierz numer stacji: ")) - 1
    if station_idx < 0 or station_idx >= len(stations):
        print("Niepoprawny numer stacji.")
        return

    station_id = stations[station_idx]['id']
    air_quality_data = get_air_quality_data(station_id)

    if not air_quality_data:
        print("Nie udało się pobrać danych o jakości powietrza.")
        return

    index_level = air_quality_data.get('stIndexLevel', {}).get('indexLevelName', 'Nieznany')
    print(f"Indeks jakości powietrza: {index_level}")

    if index_level == "Bardzo dobry":
        print("Jakość powietrza jest bardzo dobra.")
    elif index_level == "Dobry":
        print("Jakość powietrza jest dobra.")
    elif index_level == "Umiarkowany":
        print("Jakość powietrza jest umiarkowana.")
    elif index_level == "Zły":
        print("Jakość powietrza jest zła.")
    elif index_level == "Bardzo zły":
        print("Jakość powietrza jest bardzo zła.")
    else:
        print("Nieznany poziom jakości powietrza.")

if __name__ == "__main__":
    main()
