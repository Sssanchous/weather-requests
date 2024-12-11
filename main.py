import requests


URL_TEMPLATE = 'https://wttr.in/{}'


def weather_forecast(location):
    url = URL_TEMPLATE.format(location)
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    locations = [
        'London',
        'airport%20Sheremetyevo',
        'Cherepovets?M?n?T&lang=ru'
    ]

    for i in locations:
        weather = weather_forecast(i)
        print(weather)


if __name__ == '__main__':
    main()