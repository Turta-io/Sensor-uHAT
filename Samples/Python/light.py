#!/usr/bin/env python3

#This sample demonstrates reading the IR and UV Index.
#Install Sensor uHAT library with "pip3 install turta-sensoruhat"

from time import sleep
from turta_sensoruhat import Turta_UV_Light

#Initialize
light = Turta_UV_Light.UVAmbientLightSensor()

try:
    while True:
        #Read UV Index
        uv = light.read_uv()

        #Read Raw IR
        ir = light.read_ir()

        #Print the readings
        print("UV Index........: " + str(round(uv, 1)))
        print("IR Raw Value....: " + str(ir))

        #Wait
        sleep(2.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
