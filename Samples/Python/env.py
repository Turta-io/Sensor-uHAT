#!/usr/bin/python

#This sample demonstrates reading temperature, relative humidity, and air pressure data.
#Install Sensor uHAT library with "pip3 install turta-sensoruhat"

import time
from turta_sensoruhat import Turta_Env_280

#Variables
#Sea level pressure in bar
slp = 1000.0 #Update this from weather forecast to get precise altitude

#Initialize
env = Turta_Env_280.EnvironmentalSensor()

try:
    while True:
        #Hint: To get temperature, pressure and humidity readings at the same time,
        #call EnvironmentalSensor.read_tph() method.

        #Read & print temperature
        print("Temperature.....: " + str(round(env.read_temperature(), 1)) + "C")

        #Read & print humidity
        print("Humidity........: %" + str(round(env.read_humidity(), 1)) + "RH")

        #Read & print pressure
        print("Pressure........: " + str(round(env.read_pressure(), 1)) + "Pa")

        #Read & print altitude
        print("Altitude........: " + str(round(env.read_altitude(slp), 1)) + "m")

        #Rest a bit
        print("-----")
        time.sleep(2.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')