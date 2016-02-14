#!/usr/bin/
# -*- coding: utf-8 -*-

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

    