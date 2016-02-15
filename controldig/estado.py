#!/usr/bin/
# -*- coding: utf-8 -*-

""" 
   estado.py - clase Estado 
   Representa estados de una máquina de estados
      
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

class Estado:
    "Representa un estado de una máquina de estados"

    def __init__(self, estado_numero, estado_salidas):
        self.numero = estado_numero
        self.salidas = estado_salidas
        self.transiciones = {}
        if estado_salidas[0] == "1":
            self.dtr = 1
        else:
            self.dtr = 0
        
        if estado_salidas[1] == "1":
            self.rts = 1
        else:
            self.rts = 0
        
    def agregar_transicion( self, entradas, destino):
        self.transiciones[entradas] = destino
        
    def dar_destino( self, entradas ):
        """devuelve el estado de destino para una transición dada
           si no existe la transición devuelve -1
        """
        try:
            dest =  self.transiciones[entradas]
        except:
            dest = -1
        
        return dest
            
    def str_estado(self):
        return self.numero, self.salidas, self.transiciones
    
    
def carga_estados(lista, nombrearchivo):
    f = open(nombrearchivo, 'r')
    for line in f:
        linea = "".join(line.split())
        linea = linea.split(",")
        e = estado.Estado(int(linea[0]), linea[1])
        
        transiciones = linea[2:]
        for t in transiciones:
            t = t.split(":")
            e.agregar_transicion(t[0],int(t[1]))
            
        lista[e.numero] = e
    f.close()
   
#e1 = Estado(1,"10")
#e2 = Estado(2,"01")
      
#print e1.str_estado()
#print e2.str_estado()

#e1.agregar_transicion("0001",1)
#e2.agregar_transicion("0001",2)
#e1.agregar_transicion("0011",2)

#e2.agregar_transicion("0100",1)
#e2.agregar_transicion("1001",2)
#e2.agregar_transicion("1001",1)

#print e1.str_estado()
#print e2.str_estado()

#print e2.dar_destino("1010")
#print e2.dar_destino("1001")

#print e1.rts
#print e1.dtr