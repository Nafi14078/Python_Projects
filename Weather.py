import requests
import json
print("Welcome to weather app created by Nafi")
city=input("Enter the city name you wish to get weather for: ")
url = f"https://api.weatherapi.com/v1/current.json?key=f3a6bdcc70c84abdb6282330250206&q={city}"
r=requests.get(url)
#print(r.text)
a=json.loads(r.text)
w=a["current"]["temp_c"]
print(w)
