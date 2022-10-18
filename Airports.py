from rich.traceback import install
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

install(show_locals = True)
import requests
import json

def airport(name):
    api_url = 'https://api.api-ninjas.com/v1/airports?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY FROM API-NINJA'})
    if response.status_code == requests.codes.ok:
        name = response.json()[0]["name"]
        country = response.json()[0]["country"]
        city = response.json()[0]["city"]
        region = response.json()[0]["region"]
        code_name = response.json()[0]["iata"]
        timezone = response.json()[0]["timezone"]
        
        info_panel = Panel(f"[b red]Name : {name}[/]\n[b]Code Name : {code_name}\nCountry : {country}\nCity : {city}\nRegion : {region}", title = f"{name}", subtitle = "  ...  ", border_style = "b green")
        print(info_panel)
    else:
        print("Error:", response.status_code, response.text)

airport()