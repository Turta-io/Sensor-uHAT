#!/usr/bin/env python3

#This sample demonstrates most of the Sensor uHATs functionality together.
#Install Sensor uHAT library with "pip3 install turta-sensoruhat"

from time import sleep
from turta_sensoruhat import Turta_Accel
from turta_sensoruhat import Turta_Env_280
from turta_sensoruhat import Turta_UV_Light

#Initialize
accel = Turta_Accel.AccelTiltSensor()
env = Turta_Env_280.EnvironmentalSensor()
light = Turta_UV_Light.UVAmbientLightSensor()

try:
    while True:
        #Read temperature, pressure, and humidity in one shot
        temperature = env.read_temperature()
        humidity = env.read_humidity()
        pressure = env.read_pressure()

        #Read X, Y and Z-Axis G values in one shot
        accel_xyz = accel.read_accel_xyz()

        #Read tilt states in one shot
        tilt_xyz = accel.read_tilt_xyz()

        #Read UV Index
        uv = light.read_uv()

        #Print the readings
        print("Temperature.....: " + str(round(temperature, 1)) + "C")
        print("Humidity........: %" + str(round(humidity, 1)) + "RH")
        print("Pressure........: " + str(round(pressure, 1)) + "Pa")

        print("X-Axis..........: " + str(round(accel_xyz[0], 2)) + "G")
        print("Y-Axis..........: " + str(round(accel_xyz[1], 2)) + "G")
        print("Z-Axis..........: " + str(round(accel_xyz[2], 2)) + "G")

        print("X-Tilt..........: " + ("Tilt detected." if tilt_xyz[0] else "No tilt."))
        print("Y-Tilt..........: " + ("Tilt detected." if tilt_xyz[1] else "No tilt."))
        print("Z-Tilt..........: " + ("Tilt detected." if tilt_xyz[2] else "No tilt."))

        print("UV Index........: " + str(round(uv, 1)))

        print("-----")

        #Wait
        sleep(1.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')