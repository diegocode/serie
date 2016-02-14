#!/usr/bin/
# -*- coding: utf-8 -*-

# invierte la tensión presente en DTR y RTS
# cada 1s y 0.25s respectivamente

import serial
import timer

# función que se ejecuta cuando 
# el timer tim_v llega al valor establecido
def led_verde(puerto):
    # invierte el estado de RTS
    puerto.rts = not puerto.rts

# función que se ejecuta cuando 
# el timer tim_r llega al valor establecido    
def led_rojo(puerto):
    # invierte el estado de DTR
    puerto.dtr = not puerto.dtr
        
# abre el puerto
s = serial.Serial("/dev/ttyUSB1")

# estado inicial de DTR y RTS (ambos -V)
s.dtr = 0
s.rts = 0

# tim_v = instancia Timer con timeout 1 s, 
# función callback led_verde 
# a la que se le pasa s como parámetro
tim_v = timer.tick_timer(1, led_verde, [s,])
# inicia timer
tim_v.start()

# tim_v = instancia Timer con timeout 1 s, 
# función callback led_verde 
# a la que se le pasa s como parámetro
tim_r = timer.tick_timer(0.25, led_rojo, [s,])
# inicia timer
tim_r.start()

while True:
    pass
    
    