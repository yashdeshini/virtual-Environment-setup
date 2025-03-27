"""
Virtual Sensor HTTP Script
--------------------------

This script simulates a virtual sensor that generates random values for:
- Temperature (°C)
- Humidity (%)
- CO2 level (ppm)

It sends the data to a ThingSpeak channel using HTTP POST requests every 30 seconds.

Requirements:
- Python 3
- requests library (Install via: pip install requests)

Configuration:
- Replace `write_api_key` with your actual ThingSpeak Write API Key.

Run:
- Execute using Python 3:
    python3 Virtual_sensor_Http.py

Stop:
- Press Ctrl+C to stop the script.
"""

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
