#!/usr/bin/
# -*- coding: utf-8 -*-

import serial
import sys
import time

# se abre port serie     
ser = serial.Serial('/dev/ttyACM0', 
                    baudrate=9600,
                    timeout=1, 
                    bytesize=serial.EIGHTBITS, 
                    parity=serial.PARITY_NONE, 
                    stopbits = serial.STOPBITS_ONE)

brillo = 0
while True:
    ser.write([brillo,])
    
    if brillo < 255:
        brillo = brillo + 1
    else:
        brillo = 0
        
    time.sleep(0.05)

    