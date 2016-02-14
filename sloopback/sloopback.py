#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import serial.tools.list_ports

import sys
import argparse

# constantes utilizadas en help y versión
PROGRAM_NAME = "serial loopback"
VERSION = "0.4"
COPYRIGHT_YEAR = 2016
PACKAGE_URL = "https://github.com/diegocode/serie/tree/master/loopback"

def print_help():
    """ Print help info. """
        
    print ( "Usage: %s [OPTION]...") % (PROGRAM_NAME)

    print "Send a message and check if the received string match."
    print "Waits for incoming chars TIMEOUT seconds"
    print "In case of TIMEOUT or messages don't match print error"
    print ""
   
    print "  -h, --help          display this help and exit"
    print "  -v, --version       display version information and exit"

    print ""
  
    print "  -p, --port=PORT        port to test: ej.: '/dev/tty0' 'COM7'"
    print "  -m, --message=MESSAGE  string to use for testing"
    print "  -t, --timeout=FLOAT    max. timeout in seconds"
    print "  -l, --list             list available serial ports"
    print "  -q, --quiet            print error messages only" 
    print ""
    
    print "  Ctrl + C - Exits"    
    print ""
    print ( "%s home page: <%s>" ) % (PROGRAM_NAME, PACKAGE_URL);   
    
    
def print_version():
    """ Print version and copyright information. """
    
    print ""
    print ("%s - %s \n")% (PROGRAM_NAME, VERSION)
    print ""

    # It is important to separate the year from the rest of the message,
    # as done here, to avoid having to retranslate the message when a new
    # year comes around.  
    print ( """Copyright (C) %d Diego Codevilla.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.\n""") % COPYRIGHT_YEAR

def list_ports():
    """ print list of available ports """
    print ""
    print "Available serial ports:"
    for p in  serial.tools.list_ports.comports():
        print p


def main():
    # create argparse object - set automatic help to false
    parser = argparse.ArgumentParser(add_help=False)
    
    # add arguments to parse 
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-v", "--version", help="",action="store_true")    
    parser.add_argument("-p", "--port", help="")
    parser.add_argument("-m", "--message", help="")
    parser.add_argument("-t", "--timeout", help="", type=float)
    parser.add_argument("-l", "--list", help="",action="store_true")
    parser.add_argument("-q", "--quiet", help="",action="store_true")
    
    # parse arguments
    args = parser.parse_args()
    
    # if --help / -h print help and exit
    if args.help:
        print_help()
        sys.exit(0)
        
    if args.list:
        list_ports()
        sys.exit(0)
    
    # if --version / -v print version information and exit
    if args.version:
        print_version()
        sys.exit(0)
    
    else:
        # if --message / -m ...
        if args.message:
            # set test message 
            msg = args.message
        else:
            msg = "D"
        
        #if --timeout / -t ...
        if args.timeout:
            # set timeout
            tout = args.timeout
        else:
            tout = 1
        
        #if --port / -p ...   
        if args.port:
            pserie = args.port
        else:
            pserie = '/dev/ttyUSB0'

    # try to open port
    # if not possible lists available ports
    try:
        ser = serial.Serial(pserie, timeout=tout)
    except serial.serialutil.SerialException, mensaje:
        print mensaje
        print "Could not open port..."

        list_ports()
        
        raise SystemExit

    
    num_err = 0
    
    print "testing port %s with message %s" % (pserie, msg)
    print "Ctrl + C to exit"
    if args.quiet:
        print "- Printing only errors"

    while True:
        # send message 
        ser.write(msg)
        
        # waits to receive as many bytes as sended
        # or continue if timeout
        rec = ser.read( len(msg) ) 
                
        if ( rec != msg ):          
            # if messages don match print error
            num_err = num_err + 1
            print "error ", num_err, rec
            
        else:
            # if messages match and not quiet prints received message
            if not args.quiet:
                print rec


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Stopping program..."
        pass
    

