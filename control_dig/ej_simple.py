#!/usr/bin/
# -*- coding: utf-8 -*-

# ejemplo senncillo de ES 
# utilizando líneas de handshaking del port serie
# requiere librería pyserial

import serial

p.cd 
p.ri 
p.dsr 
p.cts 
        s.rts = estados[e].rts
        s.dtr = estados[e].dtr
  
# abrir puerto  
ser = serial.Serial("/dev/ttyUSB0", timeout=1) 
    
# fijar estado de las salidas
ser.rts = True
ser.dtr = False

# leer estado de entradas
print ser.cd, ser.ri, ser.dsr, ser.cts

# cerrar port
ser.close()