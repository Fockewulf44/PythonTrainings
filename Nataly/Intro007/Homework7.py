import requests, json

class HourlyTemp:
    minimum_temp = 0
    max_temp = 0
    def __init__(self) -> None:
        self.getHourlyTemp()
    
    def getHourlyTemp(self):
        result = requests.get("https://dataservice.accuweather.com/forecasts/v1/daily/1day/347626?apikey=93dEYuLNl9RGleWNeGdAa5Z6Ch4CfZuT")
        text = result.text
        j = json.loads(text)
        array_0 =j["DailyForecasts"] [0]
        temp = array_0["Temperature"]
        self.minimum_temp = temp["Minimum"] ["Value"]
        self.max_temp = temp["Maximum"] ["Value"]
    
    def TodaysTemp(self):
        print(f"Today's forecast has a low of {self.minimum_temp}")
p = HourlyTemp()
p.TodaysTemp()
v = 100
