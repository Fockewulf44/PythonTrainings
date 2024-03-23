# March 23rd Class
# https://docs.google.com/document/d/1edWaqH1-ePTHMUo9KmD229s599iMhUaj-kRDnkavbv4/edit?pli=1
# https://docs.google.com/document/d/16IQ96cfTaXEHRDuZPp1DhFEUYgZvuTrQUxnwJ3LfYbA/edit

# Watch Step into Wix Studio | The web platform for agencies and enterprises (youtube.com)
# Watch Top 10 Git Commands | Most Used Git Commands | Git Commands With Examples | Simplilearn (youtube.com)
# Use git commands:
# Git pull
# Git Merge
# Git Fetch
# Git commit
# Git checkout
# Make sure that you are comfortable and understand git commands above

# Exercise:
# Create a class to provide weather condition by using accuweather API.
# Class must have:
# Properties like maximum, minimum temperatures
# Property - today’s date
# Function that prints(use f string) like today’s max and min temperatures are …
# Function that prints today's condition from Headline node. Example: "Patchy fog will affect the area from late tomorrow night to Monday morning"
# Property hourly forecast. Create a new class for that and add properties - datetime, temperature, iconphrase.
# Function that would print hourly forecast.

import requests, json

class DailyForecast:
    minimum_temp = 0
    max_temp = 0
    
    def __init__(self) -> None:
        self.getDailyForecast()
        
    def getDailyForecast(self):
        result = requests.get(
            "http://dataservice.accuweather.com/forecasts/v1/daily/1day/347626?apikey=93dEYuLNl9RGleWNeGdAa5Z6Ch4CfZuT"
        )
        text = result.text
        j = json.loads(text)
        array_0 = j["DailyForecasts"][0]
        
        temp = array_0["Temperature"]
        
        self.minimum_temp = temp["Minimum"]["Value"]
        self.max_temp = temp["Maximum"]["Value"]
        
    def TodaysTemp(self):
        print(f"Today's forecast has a low of {self.minimum_temp} and a high of {self.max_temp}")
        
p = DailyForecast()
p.TodaysTemp()