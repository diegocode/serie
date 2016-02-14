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
    # solicita ingreso de cantidad desde teclado
    cant = raw_input("cuántos asteriscos? ")
    
    # envía por puerto serie el string ingresado
    ser.write( cant);
        
    while True:
        # lee lo recibido por el puerto serie
        rec = ser.read()
        
        linea = linea + rec
        if rec == '\n':        
            # si es fin de línea, muéstra por pantalla
            print linea
            linea = ""
            break


        
    
    