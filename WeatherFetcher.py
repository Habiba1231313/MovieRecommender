import requests
class WeatherFetcher:
    def __init__(self,city):
        self.api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = "b3b48187861891a3c3d52c306ca5b7ee"
        self.city = city
       
    def fetch_weather(self):
        url = f"{self.api_endpoint}?q={self.city}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error fetching data")
    def format_weather(self):
        data = self.fetch_weather()
        if data is None:
            print("Failed to fetch weather data.")
        else:
            print("Weather in " + self.city)
            print("Temperature: " + str(data['main']['temp'] - 273) + 'Celsius')
            print("Describtion: " + data["weather"][0]["description"])
            print("Humidity: " + str(data["main"]["humidity"]))
        
    def temperature(self):
        data = self.fetch_weather()
        if data is None:
            print("Failed to fetch weather data.")
        else:
            return data['main']['temp'] - 273
            