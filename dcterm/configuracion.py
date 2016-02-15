#!/usr/bin/
# -*- coding: utf-8 -*-

""" 
   configuracion.py - clase para manejar la configuración a partir de un archivo
   
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

class Configuracion:
    "Representa una configuración determinada"
    def __init__(self, f):
        self.puerto = puerto = '/dev/ttyUSB0'
        self.t_scan = 2
        self.archivo_estados = "prueba.scd"
        self.archivo_configuracion = f
        self.archivo_registro = ""
        self.reg_solo_cambios = "1"
        self.reg_fecha = "0"
        self.reg_hora = "0"
        self.reg_separador = ","
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
            elif arg == "archivo_registro":
                self.archivo_registro = val
            elif arg == "archivo_estados":
                self.archivo_estados = val
            elif arg == "registro_solo_cambios":
                self.reg_solo_cambios = val
            elif arg == "registro_fecha":
                self.reg_fecha = val
            elif arg == "registro_hora":
                self.reg_hora = val        
            elif arg == "registro_separador":
                self.reg_separador = val                    
            elif arg == "estado_inicial":
                self.estado_inicial = int(val)
                #print "***"
            
            #print arg, val


#c = Configuracion("prueba.cfg")
#c.cargar_configuracion()

#print c.estado_inicial, c.puerto, c.archivo_estados, c.t_scan 