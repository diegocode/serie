#!/usr/bin/
# -*- coding: utf-8 -*-

import serial
import sys

try:
    # se abre port serie     
    ser = serial.Serial('/dev/ttyACM0', 
                    baudrate=9600,
                    timeout=1, 
                    bytesize=serial.EIGHTBITS, 
                    parity=serial.PARITY_NONE, 
                    stopbits = serial.STOPBITS_ONE)
except serial.serialutil.SerialException, mensaje:
    print mensaje
    print "No se puede continuar con la ejecución"
    raise SystemExit


while True:
    rec = ser.read() 
    if len(rec) < 1:
        print "error en comunicaciones"
        
    sys.stdout.write(rec)

    