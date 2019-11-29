import time
import datetime
import traceback

import requests
import RPi.GPIO as GPIO

from lib.DHT11_Python.dht11 import DHT11
from settings import *

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

def main():
    # read data using pin 14
    instance = DHT11(pin=14)

    before_time = 0
    try:
        while True:
            elapse_time = time.time() - before_time
            if(elapse_time < SAMPLING_INTERVAL_SEC):
                time.sleep(SAMPLING_INTERVAL_SEC - elapse_time)
            before_time = time.time()
            sendDataToGas(instance)
    except:
        traceback.print_exc()
        GPIO.cleanup()
        print("Cleanup")

def sendDataToGas(instance):
    result = instance.read()
    if result.is_valid():
        data = {"timestamp": str(datetime.datetime.now()), "pi_id": PI_ID, "temperature": "%-3.1f" % result.temperature, "humidity": "%-3.1f" % result.humidity}
        response = requests.post(GAS_URL, data=data)
        print("Last valid input: " + data["timestamp"])
        print("Temperature: " + data["temperature"])
        print("Humidity: " + data["humidity"])
        print("Response status: %d" % response.status_code)
    else:
        print(str(datetime.datetime.now()) + " Result data is INVALID")

if __name__ == "__main__":
    main()