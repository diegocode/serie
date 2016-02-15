#!/usr/bin/
# -*- coding: utf-8 -*-

""" 
   hndsh-01.py 
   
   fija tensión positiva y negativa alternativamente 
   cada 500 ms en la pata RTS

   
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
