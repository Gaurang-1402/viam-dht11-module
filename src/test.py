import RPi.GPIO as GPIO
import dht11
import time

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Read data using pin 4
myDHT = dht11.DHT11(pin=17)

try:
    while True:
        result = myDHT.read()
        if result.is_valid():
            print(f"Temperature: {result.temperature} C")
            print(f"Humidity: {result.humidity} %")
        else:
            print(result)
            print("Read error or no valid result.")
        time.sleep(.2)  # Sleep for 2 seconds to prevent excessive reads
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Cleanup and exit.")
