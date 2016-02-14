#!/usr/bin/
# -*- coding: utf-8 -*-

# envía un byte cada 100 ms 
# el byte comienza en cero 
# y se incrementa en 1 hasta 255

# funciona con el ejemplo Dimmer de Arduino

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
    # envía el valor brillo
    ser.write([brillo,])
    
    # si brillo es menor a 255
    # le suma uno.
    # si es 255 brillo = 0
    if brillo < 255:
        brillo = brillo + 1
    else:
        brillo = 0

    # hace un retardo (bloqueante) de 100 ms aprox.
    time.sleep(0.1)

    