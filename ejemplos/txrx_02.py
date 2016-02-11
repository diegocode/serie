#!/usr/bin/
# -*- coding: utf-8 -*-

import serial

# se abre port serie     
ser = serial.Serial('/dev/ttyACM1', 
                    baudrate=9600,
                    timeout=2, 
                    bytesize=serial.EIGHTBITS, 
                    parity=serial.PARITY_NONE, 
                    stopbits = serial.STOPBITS_ONE)

rec = ""
linea = ""
while True:
    cant = raw_input("cuántos asteriscos? ")
    ser.write( cant);
    
    while True:
        rec = ser.read()
        linea = linea + rec
        if rec == '\n':        
            print linea
            linea = ""
            break


        
    
    