# HW7
# Class model
class DailyForecast:
    max_temperature=0
    min_temperature=0
    forecast_date=None

# Class model
class HourlyForecast:
    datetime=None
    temperature=0
    iconphrase=""
    
class WeatherCondition:
    
    daily_forecast_response=""
    hourly_forecast_response=""
    
    #DailyForecast
    daily_forecast:DailyForecast
    
    # list of HourlyForecast
    hourly_forecast = []
    
    def ExampleMethod(self):
        HourlyForecast1 = HourlyForecast()
        HourlyForecast1.temperature=100
        HourlyForecast1.iconphrase="Pretty foggy"
        
        self.hourly_forecast.append(HourlyForecast1)
        
        return None
    
    def __init__(self) -> None:
        # call here ONLY getDailyForecast
        # and getHourlyForecast
        pass
    
    def getDailyForecast():
        # Call the DailyForecastAPI 
        # and save result in self.daily_forecast_response
        pass
    
    def getHourlyForecast():
        # Call the HourlyForecastAPI 
        # and save result in self.hourly_forecast_response
        pass
    
    def ParseDailyForecastResponse():
        # Parse self.daily_forecast_response 
        # and save it in a new variable daily_Forecast
        pass
        
    def ParseHourlyForecastResponse():
        # Parse self.hourly_forecast_response 
        # and save it in a new variable hourly_Forecast
        pass
        
        for i in range(100):
            hourly_forecast.append(HourlyForecast())
            

    def PrintTodaysDailyTemp():
        print()
        
    def PrintTodaysHourlyTemp():
        print()
        