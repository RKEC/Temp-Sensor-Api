from flask import *
import RPi.GPIO as GPIO
import dht11
import json
import time
import datetime

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=17)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    result = instance.read()
    if result.is_valid():

        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)

    time.sleep(5)
    data_set = {'Temp': result.temperature, 'Humidity': result.humidity, 'Timestamp': str(datetime.datetime.now())}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)