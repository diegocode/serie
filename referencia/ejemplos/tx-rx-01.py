#!/usr/bin/
# -*- coding: utf-8 -*-


""" 
   tx-rx-01.py 
   
   Permite enviar por puerto serie un string ingresado por teclado
   Y muestra en pantalla lo recibido. 

   puede funcionar con el ejemplo tx-rx-01.ino (Arduino)
   
   
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


        
    
    