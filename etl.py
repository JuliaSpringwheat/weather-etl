#import csv

#with open("customers.csv", "r") as file:
#	data = list(csv.DictReader(file))

#print(data)

#usa_customers = [customer for customer in data if customer["country"] == "USA"]

#print(usa_customers)

#with open("usa_customers.csv", "w", newline="") as file:
#    writer = csv.DictWriter(file, fieldnames=["name", "age", "country"])
#    writer.writeheader()
#    writer.writerows(usa_customers)

import requests

response = requests.get("https://api.weather.gov/points/28.5383,-81.3792"
)

data = response.json()
forecast_response = requests.get(data["properties"]["forecast"])
forecast_data = forecast_response.json()

weather_data = []

for period in forecast_data["properties"]["periods"]:
    weather = {
        "Period": period["name"],
        "Start": period["startTime"],
        "Temperature": period["temperature"],
        "Forecast": period["shortForecast"]
    }

    weather_data.append(weather)

print(weather_data)

import csv

with open("weather_forecast.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=weather_data[0].keys())
    writer.writeheader()
    writer.writerows(weather_data)