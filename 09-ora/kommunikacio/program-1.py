import requests
import time

url = "https://api.open-meteo.com/v1/forecast?latitude=47.53&longitude=21.62&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum&timezone=Europe%2FBerlin"


def main():
    res = requests.get(url)
    json_data = res.json()["daily"]

    headers = ["time",
               "temperature_2m_max",
               "temperature_2m_min",
               "sunrise",
               "sunset",
               "precipitation_sum"
               ]

    start = time.time()

    with open('weather.txt', 'w') as f:
        for header in headers:
            f.write(f"{header}\n")
            for item in json_data[header]:
                f.write(f"{item}\n")

    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
