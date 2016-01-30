#!/usr/bin/
# -*- coding: utf-8 -*-

# v.1 - Representa la configuración 

class Configuracion:
    "Representa una configuración determinada"
    def __init__(self, f):
        self.puerto = puerto = '/dev/ttyUSB0'
        self.t_scan = 2
        self.archivo_estados = "prueba.scd"
        self.archivo_configuracion = f
        self.estado_inicial = 0
        self.nombres = {"DCD": "DCD", "RI":"RI", "DSR":"DSR", "CTS":"CTS", "RTS":"RTS", "DTR": "DTR"}
       
    def cargar_configuracion(self):
        f = open(self.archivo_configuracion, 'r')
        for linea in f:
            arg = linea.split("=")[0].strip()
            val = linea.split("=")[1].strip()
            
           
            if arg == "puerto":
                self.puerto = val
            elif arg == "tscan":
                self.t_scan = float(val)
            elif arg == "archivo_estados":
                self.archivo_estados = val
            elif arg == "estado_inicial":
                self.estado_inicial = int(val)
                #print "***"
            
            #print arg, val


#c = Configuracion("prueba.cfg")
#c.cargar_configuracion()

#print c.estado_inicial, c.puerto, c.archivo_estados, c.t_scan 