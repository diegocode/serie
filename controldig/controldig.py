#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# monitorea y fija estados  de las líneas de handshaking del puerto serie
# en forma manual o de acuerdo a un script

import serial
import time

import timer
import estado
import configuracion
import registro

# para mostrar nombres descriptivos en lugar de los nombres de los pines
#nombres={"DCD": "Puerta", "RI":"Ventana", "DSR":"Activado", "CTS":"Movimiento", "RTS":"Llamada", "DTR": "Sirena"}
#nombres={"DCD": "DCD", "RI":"RI", "DSR":"DSR", "CTS":"CTS", "RTS":"RTS", "DTR": "DTR"}

estado_actual = 0

def is_set(a, mascara):
    """devuelve como string el estado del bit especificado por <mascara>"""
    if (( a & mascara ) != 0 ):
        return "1"
    else:
        return "0"

def get_inp_status(p):
    """devuelve como entero el estado de las entradas"""
    return p.cd * 0x80 + p.ri * 0x40 + p.dsr * 0x20 + p.cts * 0x10 

def get_inp_status_str(n):
    return  is_set(n, 0x80) + is_set(n, 0x40) + is_set(n, 0x20) + is_set(n, 0x10)

def get_out_status(p):
    """devuelve como entero el estado de las salidas"""
    return p.dtr * 0x02 + p.rts * 0x01

def get_fmt_inp_status(n):
    """devuelve un string con el estado de las entradas"""
    return "DCD-> " + is_set(n, 0x80) + " RI-> " + is_set(n, 0x40) + " DSR-> " + is_set(n, 0x20) + " CTS-> " + is_set(n, 0x10)  

def get_fmt_out_status(n):
    """devuelve un string con el estado de las salidas"""
    return "DTR-> " + is_set(n, 0x02) + " RTS-> " + is_set(n, 0x01)

def get_fmt_status(p):
    """devuelve un string con el estado de las entradas y salidas """
    
    # obtiene estado de entradas y salidas
    entradas = get_inp_status(p)
    salidas = get_out_status(p)
    # muestra estado por consola 
    return  get_fmt_inp_status(entradas) + "   " + get_fmt_out_status(salidas)
     
def reemplazar_nombres(s, nombres): 
    """asigna los nombres descriptivos a las patas"""
    for n in nombres:
        s = s.replace(n, nombres[n])
    return s 
 
def carga_estados(lista, nombrearchivo):
    """carga estados definidos en el archivo de script"""
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

def timeout_scan( s, estados, c, log ):    
    """callback del timer - se ejecuta cada t_scan"""
    global estado_actual
    
    ent = get_inp_status(s)
        
    entradas_str = get_inp_status_str(ent)
    e = estados[estado_actual].dar_destino(entradas_str)
    
    #print estado_actual, e, entradas_str, estados[estado_actual].transiciones
    
    # cambia de estado las salidas si corresponde 
    # segun el estado de las entradas 
    if (e != estado_actual) and (e != -1):
        estado_actual = e
        s.rts = estados[e].rts
        s.dtr = estados[e].dtr
    
    datos = str(estado_actual) + " - " + reemplazar_nombres(get_fmt_status(s), c.nombres) 
    print datos
    
    # si se configuró nombre de archivo de registro
    # guarda línea en el log
    if c.archivo_registro != "":
        log.guardar_linea([datos,])


def main():
    global estado_actual
    
    estados = {}  
    
    # instancia de Configuracion 
    c = configuracion.Configuracion("controldig.cfg")
    # carga confiiguración del archivo especificado
    c.cargar_configuracion()  
   
    try:
        #crea instancia de Serial y abre puerto
        ser = serial.Serial(c.puerto, timeout=1) 
    except serial.serialutil.SerialException, mensaje:
        # si no se puede abrir el puerto, termina la aplicación
        print mensaje
        print "No se puede continuar con la ejecución"
        raise SystemExit
    
    # carga el script para modo automático
    carga_estados(estados, c.archivo_estados)
    
    # estado inicial
    try: 
        salidas = estados[c.estado_inicial].salidas      
        ser.dtr = estados[c.estado_inicial].dtr
        ser.rts = estados[c.estado_inicial].rts
        estado_actual = c.estado_inicial
    except KeyError:
        print "no se especificó un estado inicial"
        estado_actual = 0
        
    # si se especificá archivo de registro
    # crea una instancia de Registrador
    if c.archivo_registro != "":
        log = registro.Registrador(c)
    else:
        log = None
        
    # inicia timer (thread) para obtener estasetdo, procesar script, log etc.
    tim = timer.tick_timer(c.t_scan, timeout_scan, [ser, estados, c, log])
    tim.start()

    while True:
        # lee comando de teclado
        cmd = ""
        cmd = raw_input().lower()

        if cmd == "d":
            print "deteniendo..."
            tim.stop()
        elif cmd == "r":
            print "reiniciando..."
            tim = timer.tick_timer(c.t_scan, timeout_scan, [ser, estados, c, log])
            tim.start()

        elif cmd == "sd":
            print "set DTR"
            ser.dtr = True
        elif cmd == "rd":
            print "reset DTR"
            ser.dtr = False	  
        elif cmd == "sr":
            print "set RTS"
            ser.rts = True
        elif cmd == "rr":
            print "reset RTS"
            ser.rts = False
        elif cmd == "s":
            print reemplazar_nombres(get_fmt_status(ser), c.nombres)
        elif cmd == "x":
            print "deteniendo y saliendo..."
            tim.stop()
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "deteniendo y saliendo..."
        pass

