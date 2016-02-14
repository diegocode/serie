#!/usr/bin/
# -*- coding: utf-8 -*-

import serial
import time

# abre el puerto
s = serial.Serial("/dev/ttyUSB1")

# estado inicial de RTS (-V)
s.rts = 0
while True:
    # si CD tiene +V...
    if s.cd:
        # invierte el estado de RTS
        s.rts = not s.rts

    # demora de 500ms
    time.sleep(0.5)

    # si RI tiene +V sale del while
    if s.ri:
        break