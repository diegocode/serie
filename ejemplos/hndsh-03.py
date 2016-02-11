#!/usr/bin/
# -*- coding: utf-8 -*-

import serial
import timer

def led_verde(puerto):
    puerto.rts = not puerto.rts
    
def led_rojo(puerto):
    puerto.dtr = not puerto.dtr
        

s = serial.Serial("/dev/ttyUSB1")
s.dtr = 0
s.rts = 0

tim_v = timer.tick_timer(1, led_verde, [s,])
tim_v.start()

tim_r = timer.tick_timer(0.25, led_rojo, [s,])
tim_r.start()

while True:
    pass
    
    