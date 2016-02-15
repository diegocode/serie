#!/usr/bin/
# -*- coding: utf-8 -*-

""" 
   rx-02.py 
   
   Muestsra en pantalla lo que recibe por puerto serie
   Con try ... except
   
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

try:
    # se abre port serie     
    # /dev/ttyACM0 
    # 9600 8-N-1 - Sin paridad 
    # timeout recepción: 1s
    ser = serial.Serial('/dev/ttyACM0', 
                    baudrate=9600,
                    timeout=1, 
                    bytesize=serial.EIGHTBITS, 
                    parity=serial.PARITY_NONE, 
                    stopbits = serial.STOPBITS_ONE)
    
except serial.serialutil.SerialException, mensaje:
    # si hubo problemas abriendo el puerto
    # muestra un mensaje de error
    # y finaliza el programa
    print mensaje
    print "No se puede continuar con la ejecución"
    raise SystemExit


while True:
    # espera recibir t=timeout un byte
    rec = ser.read()        
    # muestra lo recibido
    sys.stdout.write(rec)

    