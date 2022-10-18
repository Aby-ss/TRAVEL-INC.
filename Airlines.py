from rich.traceback import install
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

install(show_locals = True)
import requests
import json

def airline(name):
    api_url = 'https://api.api-ninjas.com/v1/airlines?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY FROM API-NINJA'})
    if response.status_code == requests.codes.ok:
        name = response.json()[0]["name"]
        fleet = response.json()[0]["fleet"]
        icao = response.json()[0]["icao"]
        info_panel = Panel(f"[b red] Name [/] : {name}\n[b] International Civil Aviation Organization Code : {icao}\n[b] Fleet : {fleet}", title = f"[b] {name}", subtitle = "  ...  ", border_style = "b green")
        print(info_panel)
    else:
        print("Error:", response.status_code, response.text)

airline()