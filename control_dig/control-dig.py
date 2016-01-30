#!/usr/bin/
# -*- coding: utf-8 -*-

# monitorea y fija estados  de las líneas de handshaking del puerto serie
# en forma manual o de acuerdo a un script

import serial
import threading
import time

import estado
import configuracion

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
    # obtiene estado de entradas y salidas
    entradas = get_inp_status(p)
    salidas = get_out_status(p)
    # muestra estado por consola 
    return  get_fmt_inp_status(entradas) + "   " + get_fmt_out_status(salidas)
     
def reemplazar_nombres(s, nombres): 
    for n in nombres:
        s = s.replace(n, nombres[n])
    return s 
 
class RepeatEvery(threading.Thread):
    """permite repetir una función cada un tiempo determinado"""
    def __init__(self, interval, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.interval = interval  # seconds between calls
        self.func = func          # function to call
        self.args = args          # optional positional argument(s) for call
        self.kwargs = kwargs      # optional keyword argument(s) for call
        self.runable = True
    def run(self):
        while self.runable:
            self.func(*self.args, **self.kwargs)
            time.sleep(self.interval)
    def stop(self):
        self.runable = False

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

def timeout_scan( s ):    
    """se ejecuta cada t_scan"""
    global estados, estado_actual, c_actual
    
    ent = get_inp_status(s)
        
    entradas_str = get_inp_status_str(ent)
    e = estados[estado_actual].dar_destino(entradas_str)
    
    #print estado_actual, e, entradas_str, estados[estado_actual].transiciones
    
    if (e != estado_actual) and (e != -1):
        estado_actual = e
        s.rts = estados[e].rts
        s.dtr = estados[e].dtr
    
    print estado_actual, reemplazar_nombres(get_fmt_status(s), c.nombres) 

c = configuracion.Configuracion("prueba.cfg")
estados = {}  

def main():
    
    #c = configuracion.Configuracion("prueba.cfg")
    c.cargar_configuracion()  
    
    #estado_actual = 0
    try:
        #crea instancia de Serial y abre puerto
        ser = serial.Serial(c.puerto, timeout=1) 
    except serial.serialutil.SerialException, mensaje:
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
    except KeyError:
        print "no se especificó un estado inicial"

    # inicia timer (thread) para obtener estasetdo, procesar script, log etc.
    th = RepeatEvery(c.t_scan, timeout_scan, ser)
    th.start()

    while True:
        cmd = ""
        cmd = raw_input().lower()

        if cmd == "d":
            print "deteniendo..."
            th.stop()
        elif cmd == "r":
            print "reiniciando..."
            th = RepeatEvery(c.t_scan, timeout_scan, ser)
            th.start()
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
            th.stop()
            break

if __name__ == '__main__':
    main()


