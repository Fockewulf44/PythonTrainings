import requests, json


class DailyForecast:
    minimum_temp = 0
    max_temp = 0

    def __init__(self) -> None:
        self.getDailyForecast()
        self.getHeadline()

    def getDailyForecast(self):
        result = requests.get(
            "https://dataservice.accuweather.com/forecasts/v1/daily/1day/347626?apikey=93dEYuLNl9RGleWNeGdAa5Z6Ch4CfZuT"
        )
        text = result.text
        j = json.loads(text)
        array_0 = j["DailyForecasts"][0]

        temp = array_0["Temperature"]

        self.minimum_temp = temp["Minimum"]["Value"]
        self.max_temp = temp["Maximum"]["Value"]

    def TodaysTemp(self):
        print(
            f"Today's forecast has a low of {self.minimum_temp} and a high of {self.max_temp}"
        )

    def getHeadline(self):
        result = requests.get(
            "https://dataservice.accuweather.com/forecasts/v1/daily/1day/347626?apikey=93dEYuLNl9RGleWNeGdAa5Z6Ch4CfZuT"
        )
        text = result.text
        j = json.loads(text)
        array_1 = j["Headline"]
        print(array_1["Text"])


class HourlyForecast:
    datetime = None
    temperature = 0
    iconphrase = ""

    def __init__(self) -> None:
        self.getHourlyForecast()

    def getHourlyForecast(self):
        result = requests.get(
            "https://dataservice.accuweather.com/forecasts/v1/hourly/12hour/347626?apikey=93dEYuLNl9RGleWNeGdAa5Z6Ch4CfZuT"
        )
        text = result.text
        j = json.loads(text)
        array_1 = j

        for i in range(len(array_1)):
            datetime = array_1[i]["DateTime"]
            temperature = array_1[i]["Temperature"]["Value"]
            iconphrase = array_1[i]["IconPhrase"]
            print([datetime, temperature, iconphrase])


class WeatherCondition:

    max_temperature = 0
    min_temperature = 0

    def __init__(self) -> None:
        self.FillInHourlyForecast()
        self.PrintTodaysTemp()

    def FillInHourlyForecast(self):
        result = requests.get(
            "https://dataservice.accuweather.com/forecasts/v1/hourly/12hour/347626?apikey=93dEYuLNl9RGleWNeGdAa5Z6Ch4CfZuT"
        )
        text = result.text
        j = json.loads(text)
        array_1 = j
        hourly_forecast = []
        for i in range(len(array_1)):
            hourly_forecast.append(HourlyForecast.getHourlyForecast(self))

    def PrintTodaysTemp(self):
        result = requests.get(
            "https://dataservice.accuweather.com/forecasts/v1/hourly/12hour/347626?apikey=93dEYuLNl9RGleWNeGdAa5Z6Ch4CfZuT"
        )
        text = result.text
        j = json.loads(text)
        array_1 = j
        print(f"The weather for {array_1[-1]['DateTime']} is {array_1[-1]['IconPhrase']} at a temperature of {array_1[-1]['Temperature']['Value']}F. ")

l = WeatherCondition()
l.FillInHourlyForecast()

l.PrintTodaysTemp()
v = 100
