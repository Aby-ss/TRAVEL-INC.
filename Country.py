from rich.traceback import install
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

install(show_locals = True)
import requests
import json

def country(name):
    api_url = f'https://api.api-ninjas.com/v1/country?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY FROM API-NINJA'})
    if response.status_code == requests.codes.ok:
        name = response.json()[0]["name"]
        population = response.json()[0]["population"]
        tourists = response.json()[0]["tourists"]
        region = response.json()[0]["region"]
        currency = response.json()[0]["currency"]["name"]
        gdp = response.json()[0]["gdp"]
        gdp_growth = response.json()[0]["gdp_growth"]
        capital = response.json()[0]["capital"]
        
        info_panel = Panel(f"[b red] Name : {name}\n Capital : {capital}\n Region : {region}[/]\n[b] GDP || GPD grwoth : {gdp} | {gdp_growth}\n Currency : {currency}\n Tourists : {tourists}", title = f"[b] {name}", subtitle = "  ...  ", border_style = "b green")
        print(info_panel)
    else:
        print("Error:", response.status_code, response.text)
        
country()