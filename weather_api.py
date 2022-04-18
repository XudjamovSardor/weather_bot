import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"


headers = {
    "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
    "X-RapidAPI-Key": "84302f1c5cmshc054e5363b83288p1ebd74jsnfcecb554094b"
}

def req(city: str):
    querystring = {"q": city, "units": "metric", "mode": "json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    info = response.json()

    return info
