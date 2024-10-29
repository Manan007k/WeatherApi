# import requests
# City = input("Enter city name: ")
# API_KEY = '8ef68bac21240cc45014cc85318d62e9'
# BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}'

# def get_weather(City):
#     params = {
#         'q': City,
#         'appid': API_KEY,
#         'units': 'metric'
#     }
#     response = requests.get(BASE_URL, params=params)
#     data = response.json()
    
#     if data['cod'] != 200:
#         return f"Error: {data['message']}"
    
#     city_name = data['name']
#     temperature = data['main']['temp']
#     weather_description = data['weather'][0]['description']
    
#     return f"City: {city_name}\nTemperature: {temperature}°C\nWeather: {weather_description}"


# print(get_weather(City))

import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = '8ef68bac21240cc45014cc85318d62e9'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['cod'] != 200:
        return f"Error: {data['message']}"

    city_name = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']

    return f"City: {city_name}\nTemperature: {temperature}°C\nWeather: {weather_description}"

def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        messagebox.showinfo("Weather Information", weather_info)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Setting up the GUI
root = tk.Tk()
root.title("Weather App")

frame = tk.Frame(root)
frame.pack(pady=10)

city_label = tk.Label(frame, text="Enter City Name:")
city_label.pack(side=tk.LEFT)

city_entry = tk.Entry(frame)
city_entry.pack(side=tk.LEFT)

get_weather_button = tk.Button(frame, text="Get Weather", command=show_weather)
get_weather_button.pack(side=tk.LEFT)

root.mainloop()

