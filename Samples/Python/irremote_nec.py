#!/usr/bin/env python3

#This sample demonstrates sending infrared remote controller messages using NEC protocol.
#Install Sensor uHAT library with "pip3 install turta-sensoruhat"

from time import sleep
from turta_sensoruhat import Turta_IRRemote

#Initialize
ir = Turta_IRRemote.IRRemoteTx()

try:
    while True:
        #Prepare the payload
        payload = [0x01, 0xFE, 0x02, 0xFD]

        #Send remote controller message in NEC protocol
        ir.write(Turta_IRRemote.PROTOCOLS.NEC, payload)

        #Print the payload
        print("IR Message Sent..: " + str(payload))

        #Wait
        sleep(2.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
