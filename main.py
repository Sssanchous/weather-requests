import requests


URL_TEMPLATE = 'https://wttr.in/{}'


def fetch_weather(location):
    url = URL_TEMPLATE.format(location)

    params = {
        'M': '',
        'n': '',
        'T': '',
        'lang': 'ru'
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.text


def main():
    locations = ['London', 'Airport Sheremetyevo', 'Cherepovets']

    for location in locations:
        weather = fetch_weather(location)
        print(weather)


if __name__ == '__main__':
    main()