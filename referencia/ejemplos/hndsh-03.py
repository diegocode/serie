#!/usr/bin/
# -*- coding: utf-8 -*-

""" 
   hndsh-03.py 
   
   invierte la tensión presente en DTR y RTS
   cada 1s y 0.25s respectivamente
   
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
    
    