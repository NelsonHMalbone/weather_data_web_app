# back end of the project
from config import api_key
import requests

api_key = api_key
def get_data(place, forecastdays, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data['list']
    nr_values = 8 * forecastdays
    filter_data = filter_data[:nr_values]
    if kind == "Temperature":
        filter_data = [dict["main"]["temp"] for dict in filter_data]
    if kind == "Sky":
        filter_data = [dict["weather"][0]['main'] for dict in filter_data]
    return filter_data

if __name__ == "__main__":
    print(get_data(place="elkton", forecastdays=3, kind='Temperature'))
    print(get_data(place="elkton", forecastdays=3, kind='Sky'))

