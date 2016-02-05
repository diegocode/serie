#!/usr/bin/
# -*- coding: utf-8 -*-

# terminal 

import serial
import time
import sys
import registro
import requests

# parámetros para configurar 
# TODO: archivo de configuración 
# TODO: parámetros línea comando

formato = "A" # H - hexa / A - ascii / D - decimal
separador_c = ""
separador_v = "_"
lineaextra = False

puerto = '/dev/ttyACM0'
baudios = 57600
timout = 1
bits_datos = serial.EIGHTBITS # FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
paridad = serial.PARITY_NONE #PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
bits_stop = serial.STOPBITS_ONE #STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO

archivo_registro = "log.txt"
reg_separador = ","
reg_fecha = "0"
reg_hora = "1"
reg_solo_cambios = "1"


try:
    # se abre port serie     
    ser = serial.Serial(puerto, 
                    baudrate=baudios,
                    timeout=timout, 
                    bytesize=bits_datos, 
                    parity=paridad, 
                    stopbits = bits_stop)
except serial.serialutil.SerialException, mensaje:
    print mensaje
    print "No se puede continuar con la ejecución"
    raise SystemExit

if archivo_registro != "":
    log = registro.Registrador(archivo_registro,
                               reg_separador,
                               reg_fecha,
                               reg_hora,
                               reg_solo_cambios
                               )
else:
    log = None
    log=None
    
if len(formato) > 1:
    #print len(formato)
    separador = separador_v
else:
    #print len(formato)
    separador = ""


linea = ""
while True:
    if ser.inWaiting():
        rec = ser.read() 
        mostrar = ""
        
        if "H" in formato:       
            hex = ("%02X") % (ord(rec))
            mostrar = mostrar + separador + hex
        
        if "A" in formato:
            mostrar = mostrar + separador + rec

        if "D" in formato:
            dec = ("%03d") % (ord(rec))
            mostrar = mostrar + separador + dec
        
        mostrar = mostrar + separador_c
        
        sys.stdout.write(mostrar)
        linea = linea + mostrar 
         
        if "A" not in formato :
            if rec == '\n':
                print
                linea = linea + '\n'
                if lineaextra:
                    print
                    linea = linea + '\n'             
                
                if archivo_registro != "":
                    log.guardar_linea([linea,])
                    
                linea = ""
        else:
            if rec == '\n':
               if lineaextra:
                    print
                    linea = linea + '\n'
                
               if archivo_registro != "":
                    log.guardar_linea([linea,])
                    
               datos = {'datos': linea}
               #requests.get("http://localhost/clima/recibe.php", params=datos)
               requests.get("http://www.diegocodevilla.com.ar/serie/clima/recibe.php", params=datos)
              
               linea = ""            

        
                
        #f = open('clima.txt', 'a')        
        #f.write(linea)   
       
        #linea = ""
        #f.close() 
        
       
       