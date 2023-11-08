import RPi.GPIO as GPIO
import dht11
import time
GPIO.setmode(GPIO.BCM)
myDHT = dht11.DHT11(pin=17)

try:
    while True:
        result = myDHT.read()
        if result.is_valid():
            print("Temperature is", result.temperature, "Humidity is", result.temperature)
        else:
            print("nothing")
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO good to go")