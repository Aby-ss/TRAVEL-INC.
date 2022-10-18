from rich import print
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.markdown import Markdown

import requests
import json

from datetime import datetime


install(show_locals = True)
con = Console()
layout = Layout()

welcome_art = """
████████╗██████╗  █████╗ ██╗   ██╗███████╗██╗         ██╗███╗   ██╗ ██████╗   
╚══██╔══╝██╔══██╗██╔══██╗██║   ██║██╔════╝██║         ██║████╗  ██║██╔════╝   
   ██║   ██████╔╝███████║██║   ██║█████╗  ██║         ██║██╔██╗ ██║██║        
   ██║   ██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║         ██║██║╚██╗██║██║        
   ██║   ██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗    ██║██║ ╚████║╚██████╗██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝    ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝
                                                                              
"""
print(welcome_art)
print(" ")

form_md = """
# WELCOME TO TRAVEL INC
#### Vacations, reimagined
### Enter the requestired details below :
"""

md = Markdown(form_md)
con.print(md)

con.print(Panel("💻                                                      TRAVEL INC.                                                               📚", border_style = "b blue"))

airline_name = Prompt.ask("Enter an airline name :")
airport_name = Prompt.ask("Enter an airport name :")
country_name = Prompt.ask("Enter a country name :")
city_name = Prompt.ask("Enter a city name :")
weather_location = country_name

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]TRAVEL INC.[/b] CLI application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")
    
# -------------------------------- MAIN FUNCTIONS -------------------------------
def airline(name):
    api_url = 'https://api.api-ninjas.com/v1/airlines?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY FROM API-NINJA'})
    if response.status_code == requests.codes.ok:
        name = response.json()[0]["name"]
        fleet = response.json()[0]["fleet"]
        icao = response.json()[0]["icao"]
        info_panel = Panel(f"[b red] Name [/] : {name}\n[b] International Civil Aviation Organization Code : {icao}\n[b] Fleet : {fleet}", title = f"[b] {name}", subtitle = "  ...  ", border_style = "b green")
        return info_panel
    else:
        print("Error:", response.status_code, response.text)

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
        return info_panel
    else:
        print("Error:", response.status_code, response.text)

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
        return info_panel
    else:
        print("Error:", response.status_code, response.text)

def cities(name):
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city_name)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY FROM API-NINJA'})
    if response.status_code == requests.codes.ok:
        name = response.json()[0]["name"]
        population = response.json()[0]["population"]
        is_capital = response.json()[0]["is_capital"]
        
        info_panel = Panel(f"[b red] Name : {name}[/]\n[b] Population : {population}\n Capital ? : {is_capital}", title = f"[b] {name}", subtitle = "  ...  ", border_style = "b green")
        return info_panel
    else:
        print("Error:", response.status_code, response.text)

def weather(name):
    
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY FROM API-NINJA'})
    if response.status_code == requests.codes.ok:
        cloud_percent = response.json()["cloud_pct"]
        temp = response.json()["temp"]
        feels_like = response.json()["feels_like"]
        Humidity = response.json()["humidity"]
        wind_speed = response.json()["wind_speed"]
        info_panel = Panel(f"[b red] Name : {name}[/]\n[b] Temperature : {temp}\n Clound % : {cloud_percent}\n Feels Like : {feels_like}\n Humidity : {Humidity}\n Wind Speed : {wind_speed}", title = f"[b] {country_name}", subtitle = "  ...  ", border_style = "b green")
        return info_panel
    else:
        print("Error:", response.status_code, response.text)

# --------------------------------------------------------------------------------

layout.split_column(
    Layout(name = "header"),
    Layout(name = "upper"),
    Layout(name = "lower"),
    Layout(name = "footer")
)

layout["upper"].split_row(
    Layout(name="upper_left"),
    Layout(name="upper_right"),
)

layout["lower"].split_row(
    Layout(name="lower_left"),
    Layout(name="lower_right"),
)

layout["header"].size = 3
layout["footer"].size = 8
layout["header"].update(Header())

layout["upper_right"].update(airline(airline_name))
layout["upper_left"].update(airport(airport_name))
layout["lower_right"].update(weather(weather_location))
layout["lower_left"].update(cities(city_name))
layout["footer"].update(country(country_name))

print(layout)



