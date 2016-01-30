#!/usr/bin/
# -*- coding: utf-8 -*-

import estado

estados = {}
archivo_estados = "prueba.scd"

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

carga_estados(estados, archivo_estados)

try: 
    print estados[3].dar_destino("0110")
except KeyError:
    print "no existe el estado especificado"
