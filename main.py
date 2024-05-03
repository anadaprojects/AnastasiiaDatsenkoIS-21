import requests # type: ignore

def get_weather(city):
    api_key = '523dfb40bdaebd1eb016b56596df1e9f'  # Підставте свій API ключ з OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    return data

# Приклад використання:
city = 'Kyiv'  # Введіть назву міста для отримання погоди
weather_data = get_weather(city)

if weather_data:
    print(f"Погода в місті {city}:")
    print(f"Температура: {weather_data['main']['temp']}°C")
    print(f"Вологість: {weather_data['main']['humidity']}%")
else:
    print("Не вдалося отримати погодні дані.")

import matplotlib.pyplot as plt

def display_weather(city, weather_data):
    if not weather_data:
        print("Не вдалося отримати погодні дані.")
        return
    
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']

    # Виведення погодних даних
    print(f"Погода в місті {city}:")
    print(f"Температура: {temp}°C")
    print(f"Вологість: {humidity}%")

    # Графічне відображення температури
    plt.figure(figsize=(8, 6))
    plt.bar(['Temperature', 'Humidity'], [temp, humidity], color=['red', 'blue'])
    plt.title(f"Weather in {city}")
    plt.ylabel("Value")
    plt.show()

# Приклад використання:
city = 'Kyiv'  # Введіть назву міста для отримання погоди
weather_data = get_weather(city)
display_weather(city, weather_data)

