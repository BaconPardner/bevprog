import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=47.31&longitude=21.62&daily=temperature_2m_max,sunrise,sunset,precipitation_sum,windspeed_10m_max&timezone=Europe%2FBerlin"

def main():
    res = requests.get(url)
    json_data = json.dumps(res.json(), indent=2) 

    with open('weather.json', 'w') as weather:
        print(json_data, file=weather)

if __name__ == "__main__":
    main()
