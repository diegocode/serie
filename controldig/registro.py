#!/usr/bin/
# -*- coding: utf-8 -*-

""" 
   registro.py - clase Registrador - Maneja registro de eventos
   
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

import time

class Registrador:
    def __init__(self, conf):
        self.nombre_archivo = conf.archivo_registro
        self.separador = conf.reg_separador
        self.flg_fecha = conf.reg_fecha
        self.flg_hora = conf.reg_hora
        self.solo_cambios = conf.reg_solo_cambios
        self.linea_anterior = ""
    
    def guardar_linea(self, datos):
        f = open(self.nombre_archivo, 'a')
        
        if self.flg_fecha == "1":
            linea = time.strftime("%Y-%m-%d") + self.separador       
            i = 11
        else:
            linea = ""
            i = 0
            
        if self.flg_hora == "1":
            linea = linea + time.strftime("%H:%M:%S") + self.separador
            i = i + 8
        else:
            linea = linea + "" 
            i = i + 0
        
        for s in datos:
            linea = linea + str(s) + self.separador
        
        linea = linea[:-1] + '\n'

        if (self.solo_cambios == "1" and self.linea_anterior[i:] != linea[i:]) or \
           (self.solo_cambios == "0"):
            
            self.linea_anterior = linea  
            f.write(linea)
        
        f.close()
        
        