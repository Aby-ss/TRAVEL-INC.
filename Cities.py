from rich.traceback import install
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

install(show_locals = True)
import requests
import json

def cities(name):
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city_name)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY FROM API-NINJA'})
    if response.status_code == requests.codes.ok:
        name = response.json()[0]["name"]
        population = response.json()[0]["population"]
        is_capital = response.json()[0]["is_capital"]
        
        info_panel = Panel(f"[b red] Name : {name}[/]\n[b] Population : {population}\n Capital ? : {is_capital}", title = f"[b] {name}", subtitle = "  ...  ", border_style = "b green")
        print(info_panel)
    else:
        print("Error:", response.status_code, response.text)
        
cities()