import os

import requests

API_KEY_YANDEX = os.getenv("API_KEY_YANDEX")


def get_coordinates(address):
    """ Функция получает адрес, делает запрос на yandex.ru и возвращает широту и долготу """
    api_key = API_KEY_YANDEX
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&format=json&geocode={address}"
    response = requests.get(url)
    data = response.json()
    if data['response']['GeoObjectCollection']['featureMember']:
        geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        point = geo_object['Point']['pos']
        lon, lat = map(float, point.split())
        return lat, lon
    return None, None
