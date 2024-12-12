import requests


URL_TEMPLATE = 'https://wttr.in/{}'


def fetch_weather(location, params):
    url = URL_TEMPLATE.format(location)
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    locations = {
        'London': '',
        'Airport Sheremetyevo': '',
        'Cherepovets': {'M': '', 'n': '', 'T': '', 'lang': 'ru'}
    }

    for location, params in locations.items():
        weather = fetch_weather(location, params)
        print(weather)


if __name__ == '__main__':
    main()