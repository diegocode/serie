#!/usr/bin/
# -*- coding: utf-8 -*-

# fija tensión positiva y negativa
# alternativamente cada 500 ms
# en la pata RTS

import serial
import time

# abre el puerto
s = serial.Serial("/dev/ttyUSB1")

# estado inicial de RTS (-V)
s.rts = 0
while True:
    # invierte el estado de RTS
    s.rts = not s.rts
    
    # demora 500ms
    time.sleep(0.5)
