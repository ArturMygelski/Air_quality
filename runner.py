from weather_data import get_air_quality_data, get_station_data, get_forecast_data, get_air_quality_index

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
    pollutants = ["PM10", "NO2", "SO2", "O3"]
    teryt_code = "1465"  # Kod TERYT dla Warszawy; zmień według potrzeb

    pollutant_levels = []
    for pollutant in pollutants:
        data = get_pollutant_data(pollutant, teryt_code)
        if data and "value" in data:
            level = data["value"]
            print(f"Stężenie {pollutant}: {level} µg/m³")
            pollutant_levels.append(level)
        else:
            print(f"Brak danych dla {pollutant}.")

    if pollutant_levels:
        air_quality_index = get_air_quality_index(pollutant_levels)
        print(f"\nOgólna jakość powietrza: {air_quality_index}")

        # Opcjonalnie, możesz wyświetlić więcej szczegółów
        print("Szczegóły:")
        for pollutant in pollutants:
            data = get_pollutant_data(pollutant, teryt_code)
            if data and "value" in data:
                level = data["value"]
                print(f"{pollutant}: {level} µg/m³ - {data.get('description', 'Brak opisu')}")


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
