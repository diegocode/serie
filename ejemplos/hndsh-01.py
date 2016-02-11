#!/usr/bin/
# -*- coding: utf-8 -*-

import serial
import time

s = serial.Serial("/dev/ttyUSB1")

s.rts = 0
while True:
    s.rts = not s.rts
    time.sleep(0.5)
