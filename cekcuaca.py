import requests

# Ganti dengan API key Anda
API_KEY = '98c28247468821fe801d1ab3565e13c0'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',  # Gunakan 'imperial' untuk Fahrenheit
        'lang': 'id'        # Bahasa Indonesia
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather(data):
    if data:
        city = data['name']
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        print(f'Cuaca di {city}:')
        print(f'Kondisi: {weather}')
        print(f'Suhu: {temp}°C')
        print(f'Kelembapan: {humidity}%')
    else:
        print('Data cuaca tidak tersedia.')

if __name__ == '__main__':
    print("Pengecek Cuaca")
    city = input('Masukkan nama kota: ')
    weather_data = get_weather(city)
    display_weather(weather_data)
