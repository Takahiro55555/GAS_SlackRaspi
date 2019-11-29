import time
import datetime

import requests
import RPi.GPIO as GPIO

from lib.DHT11_Python.dht11 import DHT11
from settings import *

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = DHT11(pin=14)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            data = {"timestamp": str(datetime.datetime.now()), "pi_id": PI_ID, "temperature": "%-3.1f" % result.temperature, "humidity": "%-3.1f" % result.humidity}
            response = requests.post(GAS_URL, data=data)

            print("Last valid input: " + data["timestamp"])
            print("Temperature: " + data["temperature"])
            print("Humidity: " + data["humidity"])
            print("Response status: %d" % response.status_code)

        time.sleep(15)

except:
    print("Cleanup")
    GPIO.cleanup()
