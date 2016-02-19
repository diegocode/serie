#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" 
   dcterminal.py - terminal serie 
   
   version 0.3
   2016.02.19
   
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
lineaextra = "0"

puerto = '/dev/ttyACM0'
baudios = 115200
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

solo_valor = "0"
valor_ini = 0
valor_fin = 5

banda_muerta_valor = 0

t_scan = 0.2

buffer = ""
linea = ""

fin = 0

def tim_func( ser, log, separador ):
    """ callback de timer """
    global linea, fin
    
    cant = ser.in_waiting
    if cant > 0:        
        # si hay bytes en buffer de recepción...
        buff = ser.read(cant) 
        mostrar = ""
            
        i = 0
        hay = 0
        mostrar = ""
        
        while i < len(buff):
            rec = buff[i]
            # mostrar = lo recibido en el formato configurado 
            # dec y/o ASCII y/o hex 
            if "H" in formato:       
                # si en formato hay H agrega car recibido en hexa
                hex = ("%02X") % (ord(rec))            
                mostrar = hex            
                hay = 1

            if "D" in formato:
                # si en formato hay D agrega car recibido en dec
                dec = ("%03d") % (ord(rec))
                if hay == 1:
                    # si hay caaracteres previos, agrega separador
                    mostrar = mostrar + separador
                    
                mostrar = mostrar + dec

            
            if "A" in formato:
                # si en formato hay A agrega car recibido en ASCII
                if hay == 1:
                    # si hay caaracteres previos, agrega separador
                    mostrar = mostrar + separador
                    
                mostrar = mostrar + separador + rec
                
                if hay == 1:
                    mostrar = mostrar + separador_v
                 
            # si se recibió fin de linea marca fin
            if rec == '\n':
                fin = 1   
                # y si no es ascii agrega fin de línea...
                if "A" not in formato:                                 
                    mostrar = mostrar + '\n'
            
            # agrega lo recibido (caracter+separadores... a línea)
            linea = linea + mostrar
            
            if fin == 1:                
                # si se recibió fin de línea realiza las acciones de línea (que correspondan):
                # separa solo valor 
                if solo_valor == "1":
                    # si se desesa guardar / mostrar solo una parte de la línea...
                    valor = linea[valor_ini:valor_fin]
                    linea = valor + '\n'

                # deja una línea extra
                if lineaextra == "1":
                    # si se desea agregar una línea extra... 
                    linea = linea + '\n'             
                    mostrar = mostrar + '\n'
                    
                # guarda la línea en archivo de registro
                if archivo_registro != "":
                    # si se configuró archivo de registro 
                    # guarda la línea
                    log.guardar_linea([linea,])                                                           

                # envía datos a web
                if destino_web_request!= "":
                    # si se configuró destino de request...
                    datos = {'datos': linea}                    
                    requests.get(destino_web_request, params=datos)
                
                linea = ""         
                fin = 0
            
            sys.stdout.write(mostrar)
            sys.stdout.flush()
            
            mostrar = ""
            i = i + 1

def mainLoop():    
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

    separador = separador_c

    linea = ""
    cmd = ""

    tim = timer.tick_timer(t_scan, tim_func, [ser,log,separador])
    tim.start()

    while True:
        # ingreso de string por teclado
        cmd = ""
        cmd = raw_input("").lower()
        
        # envía el string ingresado
        ser.write(cmd)           
         
if __name__ == '__main__':
    try:
        mainLoop()
    except KeyboardInterrupt:
        print "deteniendo aplicación..."
        pass
        
       
       