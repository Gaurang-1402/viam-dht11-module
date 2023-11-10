import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional
from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
import dht11
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Define the GPIO pin where the sensor is connected
DHT_PIN = 4  # GPIO pin number where the sensor is connected

# Create an instance of the DHT11 sensor
sensor_instance = dht11.DHT11(pin=DHT_PIN)

class MySensor(Sensor):
    # Define the model of the sensor
    MODEL: ClassVar[Model] = Model(ModelFamily("nyu", "gaurang-dht11-module"), "linux")

    # Initialize the sensor with the name provided in the configuration
    def __init__(self, name: str):
        super().__init__(name)

    # Create a new instance of the sensor using the configuration
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> "MySensor":
        sensor = cls(config.name)
        return sensor

    # Read the humidity and temperature from the sensor
    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        result = sensor_instance.read()
        if result.is_valid():
            return {"temperature": result.temperature, "humidity": result.humidity}
        else:
            return {"error": result.error_code}

async def main():
    # Create a new sensor object and get readings
    my_sensor = MySensor(name="dht11_sensor")
    readings = await my_sensor.get_readings()
    print(readings)

# Run the main function when the script is executed
if __name__ == '__main__':
    asyncio.run(main())
