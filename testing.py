import requests
api_url = f'https://api.openweathermap.org/data/2.5/weather?appid=32544a9752c598380e82439fb92a749c&q=Lahore'
show_in_json_format = requests.get(api_url).json()
weather_desc = show_in_json_format['weather'][0]['description']
weather_temp = show_in_json_format['main']['temp']
print(weather_desc)
print(weather_temp)