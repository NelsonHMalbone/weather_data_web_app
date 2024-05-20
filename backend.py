# back end of the project
from config import api_key
import requests

api_key = api_key
def get_data(place, forecastdays):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data['list']
    nr_values = 8 * forecastdays
    filter_data = filter_data[:nr_values]
    return filter_data

if __name__ == "__main__":
    print(get_data(place="elkton", forecastdays=3))


