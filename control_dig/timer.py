#!/usr/bin/
# -*- coding: utf-8 -*-

# v.1 - Representa la configuración 

from threading import Timer

class tick_timer():
    def __init__(self, inte, fnc, arg):     
        self.intervalo = inte
        self.argumentos = arg
        self.funcion = fnc
        self.contando = 1
    
    def timeout(self):
        self.contando = 0
        self.funcion(*self.argumentos)
        self.timer = Timer(self.intervalo,self.timeout)
        self.timer.start()
        self.contando = 1
        
    def start(self):
        self.timeout()
        
    def stop(self):
        if self.contando == 1:
            self.timer.cancel()
            self.contando = 1

def proceso(a, b):
        print a * b

def otro(x, y, z):
        print "otro->", x+y+z


if __name__ == '__main__':
    a = 95
    c = 2.36
    
    x=tick_timer(0.5,proceso, [a, c])
    x.start()
     
    x2=tick_timer(3,otro, [5, 2, c])
    x2.start() 
    
    a = ''
    while a != 'x':
        a = raw_input('>')
        print "-------", a
        
    x.stop()
    x2.stop()