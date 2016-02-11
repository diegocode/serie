#!/usr/bin/
# -*- coding: utf-8 -*-

import serial
import time

s = serial.Serial("/dev/ttyUSB1")

s.rts = 0
while True:
    if s.cd:
        s.rts = not s.rts
        
    time.sleep(0.5)

    if s.ri:
        break
    
    
    