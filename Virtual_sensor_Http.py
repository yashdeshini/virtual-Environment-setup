import requests
import random
import time

write_api_key = "ROHYNF3G91SG0NB1" 
channel_url = "https://api.thingspeak.com/update"

while True:
    temperature = round(random.uniform(-50, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    co2 = round(random.uniform(300, 2000), 2)

    response = requests.post(channel_url, params={
        'api_key': write_api_key,
        'field1': temperature,
        'field2': humidity,
        'field3': co2
    })

    print("Posted:", temperature, humidity, co2, "| Response:", response.text)
    time.sleep(30)