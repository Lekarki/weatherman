import datetime as dt
import requests
import typer
import random

app = typer.Typer()

BASE_CITY = "http://api.openweathermap.org/geo/1.0/direct?q="
BASE_URL ="https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()


@app.command()
def weather(location: str):

    CITY = location

    city_url = BASE_CITY + CITY + "&limit=5&appid=" + API_KEY

    user_iq = random.randint(1, 199)

    latlon = requests.get(city_url).json()
    lat = str(latlon[0]['lat'])
    lon = str(latlon[0]['lon'])
    # print(lat)
    # print(lon)

    url = BASE_URL + "lat=" + lat + "&lon=" + lon + "&appid=" + API_KEY
    response = requests.get(url).json()

    def kelvin_to_celcius_fahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

    country = latlon[0]['country']
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celcius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    time_of_calc = dt.datetime.utcfromtimestamp(response['dt'] + response['timezone'])

    print("")
    print(f"\u001b[1mUser IQ is:\u001b[0m {user_iq}")
    print("")
    print(f"\u001b[1mCity/Country:\u001b[0m {CITY}, {country}")
    print(f"\u001b[1mTemperature in {CITY}:\u001b[0m {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"\u001b[1mTemperature in {CITY} feels like:\u001b[0m {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
    print(f"\u001b[1mHumidity in {CITY}:\u001b[0m {humidity}%")
    print(f"\u001b[1mWind Speed in {CITY}:\u001b[0m {wind_speed}m/s")
    print(f"\u001b[1mWeather in {CITY}:\u001b[0m {description}")
    print(f"\u001b[1mSun rises in {CITY} at\u001b[0m {sunrise_time} \u001b[1mlocal time.\u001b[0m")
    print(f"\u001b[1mSun sets in {CITY} at\u001b[0m {sunset_time} \u001b[1mlocal time.\u001b[0m")
    print(f"\u001b[1mCalculated at:\u001b[0m {time_of_calc} \u001b[1mlocal time.\u001b[0m")

@app.command()
def weatherMan(location: str):

    CITY = location

    city_url = BASE_CITY + CITY + "&limit=5&appid=" + API_KEY

    user_iq = random.randint(1, 199)

    latlon = requests.get(city_url).json()
    lat = str(latlon[0]['lat'])
    lon = str(latlon[0]['lon'])
    # print(lat)
    # print(lon)

    url = BASE_URL + "lat=" + lat + "&lon=" + lon + "&appid=" + API_KEY
    response = requests.get(url).json()

    def kelvin_to_celcius_fahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

    country = latlon[0]['country']
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celcius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    time_of_calc = dt.datetime.utcfromtimestamp(response['dt'] + response['timezone'])

    # Säämies print
    print(r"""
⣿⣿⣿⣿⣿⠛⢿⣿⣿⣿⣿⣿⣿⡇⣾⣿⣿⣷⡌⢹⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣇⠠⢼⣆⢻⣿⣿⣿⣿⣿⠇⣿⣿⣿⣿⠇⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣷⣌⠻⢆⣉⡉⣉⠛⢡⣼⣿⣿⣿⣧⠌⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⣆⠙⣿⣿⣷⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢻⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣏⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⣧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣭⣝⠻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⣻⣿⣿⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠻⠟⠟⠳⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠂⠴⠘⣾⠤⣨⡇⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠟⠛⠛⠂⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠘⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠲⠶⣿⣿⣿⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⡿⢁⣼⣿⣿⣿⣿⣶⡌⣿⣿⣿⣿⣿⣿⣿⡏⣰⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣻⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⡟⢁⣾⣿⣿⣿⣿⣿⡿⢁⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⢋⡉⢀⡀⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⡇⢸⣿⣿⣿⣿⡿⠋⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⣴⠀⠀⠀⠀⠀⠊⢻⠆⠁⣲⢭⢥⠄⡀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⠟⣠⣾⣿⣿⣿⠟⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠌⣿⣿⠀⠀⠀⢠⢎⡠⠀⢠⢀⡀⢀⠇⢂⠲⣧⢢⣜⣉⡿⠎⠢⠙⡷⣄⠀⠀⠀⠀⠀
⠛⣡⣾⣿⣿⣿⠿⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠠⣿⣿⠀⠀⠐⠓⠛⠁⢠⠌⡾⠁⢀⣾⢜⠫⢁⡏⠔⠎⠏⣸⠿⢢⠀⠈⠀⠀⠀⠀⠀
⣾⣿⣿⡿⠛⠋⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠹⠀⠀⠰⠘⠀⠋⠿⣠⢀⡤⣾⣥⣾⡀⣨⣛⠲⠏⢠⡐⠂⠃⢂⠂⣤⠀⠀⠀⠀
⣿⣿⣿⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢆⠀⡠⠶⡤⢉⠀⡘⠋⡉⠘⠀⢍⠉⠗⢀⣤⡉⠁⠆⠀⠀⠇⠂⠀⠀⠀
⣿⣿⡏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣠⠀⠀⠀⠘⡅⣰⠃⡍⣚⣛⣆⢋⡔⠃⣸⡆⡀⡸⠋⠻⢀⢠⠀⠀⠸⡷⠀⠀⠀
⣿⣿⣧⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣰⣿⠀⠠⠀⠁⠰⠀⠆⡱⢋⠩⣥⣚⠃⣴⠐⠄⣇⠇⣤⡄⠀⣆⢀⢈⣀⢻⡆⠀⠀
⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿⠀⠀⠜⣱⢂⠈⠐⡂⠚⣀⣙⡏⠒⠲⡬⠙⠈⢀⡈⠀⣊⠅⡜⡸⠟⠈⠏⠀⠀
⣿⣿⡟⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢡⣿⣿⣿⣿⠀⡹⠋⠂⡎⠘⡀⢰⠾⣩⣓⣃⠂⠴⠂⠈⠃⠈⣀⡄⠘⠀⠀⣍⣈⣼⠃⡆⠀
⣿⣿⠇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠴⣿⣿⣿⣿⣿⢀⣷⡇⡀⡅⣦⠘⡋⢀⡏⠐⡎⡇⣿⡟⢡⡼⠀⣈⠀⠀⣞⣤⠉⢭⠴⠀⠁⠀
⣿⣿⣆⠙⢿⣿⣿⣿⣿⣿⣿⡿⠛⣉⣉⣤⣶⣶⣶⣦⡘⠛⠻⠿⣿⠈⠛⠁⢡⣠⣏⢼⡇⠘⠷⢬⣴⡇⢹⣘⠂⢱⡆⡙⠦⠤⣭⣶⣿⡟⡀⠀⠀⠀
⣿⣿⣿⣷⣦⠸⠿⠿⢛⣉⣴⣾⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠥⠤⠿⢀⡀⠠⠌⠾⣿⠿⠻⡆⣿⠷⣶⡄⠬⠭⠵⠮⠷⠟⠈⢰⡛⠛⠛⠁⠀⠀⠀⠀""")
    # print("")
    # print(f"\u001b[1mUser IQ is:\u001b[0m {user_iq}")
    print("")
    print(f"\u001b[1mCity/Country:\u001b[0m {CITY}, {country}")
    print(f"\u001b[1mTemperature in {CITY}:\u001b[0m {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"\u001b[1mTemperature in {CITY} feels like:\u001b[0m {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
    print(f"\u001b[1mHumidity in {CITY}:\u001b[0m {humidity}%")
    print(f"\u001b[1mWind Speed in {CITY}:\u001b[0m {wind_speed}m/s")
    print(f"\u001b[1mWeather in {CITY}:\u001b[0m {description}")
    print(f"\u001b[1mSun rises in {CITY} at\u001b[0m {sunrise_time} \u001b[1mlocal time.\u001b[0m")
    print(f"\u001b[1mSun sets in {CITY} at\u001b[0m {sunset_time} \u001b[1mlocal time.\u001b[0m")
    print(f"\u001b[1mCalculated at:\u001b[0m {time_of_calc} \u001b[1mlocal time.\u001b[0m")

@app.command()
def apina():
    print('apina')


if __name__ == "__main__":
    app()
 