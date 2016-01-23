#!/usr/bin/
# -*- coding: utf-8 -*-

# permite hacer loopback para testear el port serie
# msg -> mensaje de prueba
# port -> puerto serie a testear

import serial

puerto = '/dev/ttyUSB0'
msg = 'Prueba del Puerto Serie ' + puerto

ser = serial.Serial(puerto) 

num_err = 0

ser = serial.Serial('/dev/ttyUSB0', timeout=1)

while True:
  ser.write(msg)
  rec = ser.read( len(msg) ) 
  if ( rec != msg ):          # read one byte
    num_err = num_err + 1
    print "timeout ", num_err, rec
    
  else:
    print rec
    

