#!/usr/bin/
# -*- coding: utf-8 -*-

""" 
   tx-01.py 
   
   envía un byte cada 100 ms 
   el byte comienza en cero 
   y se incrementa en 1 hasta 255

   funciona con el ejemplo Dimmer de Arduino/Examples
   
   Copyright 2016 - Diego Codevilla - <dcodevilla@pioix.edu.ar>
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  
"""

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

    