#!/usr/bin/
# -*- coding: utf-8 -*-

# monitorea y fija estados  de las líneas de handshaking del puerto serie
# en forma manual o de acuerdo a un script

import serial
import threading

from timeit import default_timer
import time

def is_set( a, mascara):
    """devuelve como string el estado del bit especificado por <mascara>"""
    if (( a & mascara ) != 0 ):
	return "1"
    else:
	return "0"

def get_inp_status(p):
    """devuelve como entero el estado de las entradas"""
    return p.cd * 0x80 + p.ri * 0x40 + p.dsr * 0x20 + p.cts * 0x10 

def get_out_status(p):
    """devuelve como entero el estado de las salidas"""
    return p.dtr * 0x02 + p.rts * 0x01

def get_fmt_inp_status(n):
    """devuelve un string con el estado de las entradas"""
    return "DCD-> " + is_set(n, 0x80) + " RI-> " + is_set(n, 0x40) + " DSR-> " + is_set(n, 0x20) + " CTS-> " + is_set(n, 0x10)  

def get_fmt_out_status(n):
    """devuelve un string con el estado de las salidas"""
    return "DTR-> " + is_set(n, 0x02) + " RTS-> " + is_set(n, 0x01)
    
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

def get_fmt_status(p):
    # obtiene estado de entradas y salidas
    entradas = get_inp_status(p)
    salidas = get_out_status(p)
    # muestra estado por consola 
    print get_fmt_inp_status(entradas), get_fmt_out_status(salidas)

def timeout_scan( s ):    
    """se ejecuta cada t_scan"""
    get_fmt_status(s)
    
def main():
    #a ingresar por consola o configuración
    puerto = '/dev/ttyUSB0'
    t_scan = 5
   
    #crea instancia de Serial 
    ser = serial.Serial(puerto) 
    #abre puerto
    ser = serial.Serial('/dev/ttyUSB0', timeout=1)  

    # tiempo inicial para calcular el tiempo de scan
    t0 = default_timer()
    
    # inicia timer (thread) para obtener estado, procesar script, log etc.
    th = RepeatEvery(t_scan, timeout_scan, ser)
    th.start()
    
    while True:
	cmd = ""
	cmd = raw_input().lower()

	if cmd == "d":
	    print "deteniendo..."
	    th.stop()
	elif cmd == "r":
	    print "reiniciando..."
	    th = RepeatEvery(t_scan, timeout_scan, ser)
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
	    get_fmt_status(ser)
	elif cmd == "x":
	    print "deteniendo y saliendo..."
	    th.stop()
	    break

if __name__ == '__main__':
    main()


