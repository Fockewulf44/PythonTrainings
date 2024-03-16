import requests, json

result = requests.get(
    "https://dataservice.accuweather.com/forecasts/v1/daily/1day/347626?apikey=93dEYuLNl9RGleWNeGdAa5Z6Ch4CfZuT"
)

text = result.text
j = json.loads(text)


array_0 = j["DailyForecasts"][0]

temp = array_0["Temperature"]

minimum = temp["Minimum"]["Value"]
maximum = temp["Maximum"]["Value"]
unit = temp["Maximum"]["Unit"]

print(f"Today's minimum is {minimum} {unit} and today's maximum is {maximum} {unit}.")

'{"Headline":{"EffectiveDate":"2024-03-18T02:00:00-07:00","EffectiveEpochDate":1710752400,"Severity":5,"Text":"Patchy fog will affect the area from late tomorrow night to Monday morning","Category":"fog","EndDate":"2024-03-18T14:00:00-07:00","EndEpochDate":1710795600,"MobileLink":"http://www.accuweather.com/en/us/oakland-ca/94612/daily-weather-forecast/347626?lang=en-us","Link":"http://www.accuweather.com/en/us/oakland-ca/94612/daily-weather-forecast/347626?lang=en-us"},"DailyForecasts":[{"Date":"2024-03-16T07:00:00-07:00","EpochDate":1710597600,"Temperature":{"Minimum":{"Value":49.0,"Unit":"F","UnitType":18},"Maximum":{"Value":69.0,"Unit":"F","UnitType":18}},"Day":{"Icon":2,"IconPhrase":"Mostly sunny","HasPrecipitation":false},"Night":{"Icon":36,"IconPhrase":"Intermittent clouds","HasPrecipitation":false},"Sources":["AccuWeather"],"MobileLink":"http://www.accuweather.com/en/us/oakland-ca/94612/daily-weather-forecast/347626?day=1&lang=en-us","Link":"http://www.accuweather.com/en/us/oakland-ca/94612/daily-weather-forecast/347626?day=1&lang=en-us"}]}'
