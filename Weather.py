from rich.traceback import install
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

install(show_locals = True)
import requests
import json

def weather(name):
    
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY FROM API-NINJA'})
    if response.status_code == requests.codes.ok:
        cloud_percent = response.json()["cloud_pct"]
        temp = response.json()["temp"]
        feels_like = response.json()["feels_like"]
        Humidity = response.json()["humidity"]
        wind_speed = response.json()["wind_speed"]
        info_panel = Panel(f"[b red] Name : {name}[/]\n[b] Temperature : {temp}\n Clound % : {cloud_percent}\n Feels Like : {feels_like}\n Humidity : {Humidity}\n Wind Speed : {wind_speed}", title = f"[b] {city_country}", subtitle = "  ...  ", border_style = "b green")
        print(info_panel)
    else:
        print("Error:", response.status_code, response.text)

weather()
