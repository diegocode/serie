#!/usr/bin/
# -*- coding: utf-8 -*-

import time

class Registrador:
    def __init__(self, archivo_registro, reg_separador, reg_fecha, reg_hora, reg_solo_cambios):
        self.nombre_archivo = archivo_registro
        self.separador = reg_separador
        self.flg_fecha = reg_fecha
        self.flg_hora = reg_hora
        self.solo_cambios = reg_solo_cambios
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
        
        