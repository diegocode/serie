#!/usr/bin/
# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports

import sys
import argparse

# Names, version, year, URLs used in help and version
PROGRAM_NAME = "serial loopback"

VERSION = "0.3"
COPYRIGHT_YEAR = 2015

PACKAGE_URL = "<https://github.com/diegocode/serie/tree/master/loopback>"

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
    parser.add_argument("-p", "--port", help="port to test")
    parser.add_argument("-m", "--message", help="message for the test")
    parser.add_argument("-t", "--timeout", help="timeout in seconds", type=float)
    parser.add_argument("-l", "--list", help="lists available ports",action="store_true")
    
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
           
        if args.port:
            pserie = args.port
        else:
            pserie = '/dev/ttyUSB0'
            
    try:
        ser = serial.Serial(pserie, timeout=tout)
    except serial.serialutil.SerialException, mensaje:
        print mensaje
        print "Could not open port..."

        list_ports()
        
        raise SystemExit

    num_err = 0

    while True:
        ser.write(msg)
        rec = ser.read( len(msg) ) 
        if ( rec != msg ):          # read one byte
            num_err = num_err + 1
            print "error ", num_err, rec
            
        else:
            print rec


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Stopping program..."
        pass
    

