#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# terminal 

import serial
import time
import sys
import registro
import requests
import timer

# parámetros para configurar 
# TODO: archivo de configuración 
# TODO: parámetros línea comando

# configuración 
formato = "A" # H - hexa / A - ascii / D - decimal
separador_c = ""
separador_v = " "
lineaextra = False

puerto = '/dev/ttyACM0'
baudios = 57600
timout = 1
bits_datos = serial.EIGHTBITS # FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
paridad = serial.PARITY_NONE #PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
bits_stop = serial.STOPBITS_ONE #STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO

archivo_registro = "log.txt"
reg_separador = ","
reg_fecha = "1"
reg_hora = "1"
reg_solo_cambios = "1"

#destino_web_request = "http://localhost/clima/recibe.php"
destino_web_request = "http://www.diegocodevilla.com.ar/serie/clima/recibe.php"
#destino_web_request = ""

valor_ini = 6
valor_fin = 10

solo_valor = "0"
banda_muerta_valor = 0

t_scan = 0.1


def tim_func():
    """ callback de timer """
    global linea
    
    if ser.inWaiting():
        # si hay bytes en buffer de recepción...
        rec = ser.read() 
        mostrar = ""
            
        # mostrar = lo recibido en el formato configurado 
        # dec y/o ASCII y/o hex 
        if "H" in formato:       
            hex = ("%02X") % (ord(rec))
            mostrar = mostrar + separador + hex
        
        if "A" in formato:
            mostrar = mostrar + separador + rec

        if "D" in formato:
            dec = ("%03d") % (ord(rec))
            mostrar = mostrar + separador + dec
        
        # le agrega al final el separador de caracteres
        mostrar = mostrar + separador_c
                
        if solo_valor == "0":
            # solo se desea mostrar todo lo recibido
            sys.stdout.write(mostrar)
            
        # va formando la línea recibida
        linea = linea + mostrar 
         
        if "A" not in formato :
            # si no se especificó formato ASCII...
            if rec == '\n':
                # ...y se recibió fin de línea 
                # deja una línea
                print
                # y agrega un caracter de fin de línea a "linea"
                linea = linea + '\n'
                                
                if lineaextra:
                    # si se desea agregar una línea extra... 
                    print
                    linea = linea + '\n'             

                if archivo_registro != "":
                    # si se configuró archivo de registro 
                    # guarda la línea
                    log.guardar_linea([linea,])
                    
                linea = ""
        else:
            # si alguno de los formato es ASCII 
            if rec == '\n':
               # y se recibió fin de línea...
               
               if lineaextra:
                    # si se desea agregar una línea extra... 
                    print
                    linea = linea + '\n'              
               
               if archivo_registro != "":
                    # si se configuró archivo de registro 
                    # guarda la línea                   
                    log.guardar_linea([linea,])
                    
               if solo_valor == "1":
                    # si se desesa guardar / mostrar solo una parte de la línea...
                    valor = linea[valor_ini:valor_fin]
                    print valor

               if destino_web_request!= "":
                    # si se configuró destino de request...
                    datos = {'datos': linea}
                    requests.get(destino_web_request, params=datos)
              
               linea = ""         

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

# si se configuró archivo de registro
# crea instancia de Registrador
if archivo_registro != "":
    log = registro.Registrador(archivo_registro,
                               reg_separador,
                               reg_fecha,
                               reg_hora,
                               reg_solo_cambios
                               )
else:
    log = None

# determina separador entre caracteres
# si se especificó más de un formato
# de visualización
if len(formato) > 1:
    separador = separador_v
else:
    separador = ""

linea = ""
cmd = ""

tim = timer.tick_timer(t_scan, tim_func, [])
tim.start()

def kbd_send():
    while True:
        while True:
            # ingreso de string por teclado
            cmd = ""
            cmd = raw_input("").lower()
            
            # envía el string ingresado
            ser.write(cmd) 
        
         
if __name__ == '__main__':
    try:
        kbd_send()
    except KeyboardInterrupt:
        print "deteniendo aplicación..."
        pass
        
       
       