#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import wx

import gettext

import serial
import controldig
import configuracion
import estado
import registro
import timer

class mainUI(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.bmpCD = wx.StaticBitmap(self.panel_2, wx.ID_ANY, wx.Bitmap("on.png", wx.BITMAP_TYPE_ANY))
        self.label_1 = wx.StaticText(self.panel_2, wx.ID_ANY, _("CD"))
        self.bmpRI = wx.StaticBitmap(self.panel_2, wx.ID_ANY, wx.Bitmap("off.png", wx.BITMAP_TYPE_ANY))
        self.label_2 = wx.StaticText(self.panel_2, wx.ID_ANY, _("RI"))
        self.bmpDSR = wx.StaticBitmap(self.panel_2, wx.ID_ANY, wx.Bitmap("off.png", wx.BITMAP_TYPE_ANY))
        self.label_3 = wx.StaticText(self.panel_2, wx.ID_ANY, _("DSR\n"))
        self.bmpCTS = wx.StaticBitmap(self.panel_2, wx.ID_ANY, wx.Bitmap("on.png", wx.BITMAP_TYPE_ANY))
        self.label_4 = wx.StaticText(self.panel_2, wx.ID_ANY, _("CTS\n"))
        self.sizer_5_staticbox = wx.StaticBox(self.panel_2, wx.ID_ANY, _("entradas"))
        self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.bmpDTR = wx.StaticBitmap(self.panel_3, wx.ID_ANY, wx.Bitmap("on.png", wx.BITMAP_TYPE_ANY))
        self.btnDTR = wx.Button(self.panel_3, wx.ID_ANY, _("DTR reset"))
        self.bmpRTS = wx.StaticBitmap(self.panel_3, wx.ID_ANY, wx.Bitmap("on.png", wx.BITMAP_TYPE_ANY))
        self.btnRTS = wx.Button(self.panel_3, wx.ID_ANY, _("RTS reset"))
        self.sizer_6_staticbox = wx.StaticBox(self.panel_3, wx.ID_ANY, _("salidas"))
        self.panel_4 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.btnScriptLoad = wx.Button(self.panel_4, wx.ID_ANY, _("cargar"))
        self.lblScriptLoad = wx.StaticText(self.panel_4, wx.ID_ANY, _(".."))
        self.btnScriptPause = wx.Button(self.panel_4, wx.ID_ANY, _("pausar"))
        self.lblScriptPause = wx.StaticText(self.panel_4, wx.ID_ANY, _("ejecutando..."))
        self.sizer_7_staticbox = wx.StaticBox(self.panel_4, wx.ID_ANY, _("script"))
        self.panel_5 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.btnLogFile = wx.Button(self.panel_5, wx.ID_ANY, _("archivo"))
        self.lblLogFile = wx.StaticText(self.panel_5, wx.ID_ANY, _(".."))
        self.btnLogPause = wx.Button(self.panel_5, wx.ID_ANY, _("pausar"))
        self.lblLogPause = wx.StaticText(self.panel_5, wx.ID_ANY, _("registrando..."))
        self.sizer_8_staticbox = wx.StaticBox(self.panel_5, wx.ID_ANY, _("registro"))
        self.panel_6 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.btnPort = wx.Button(self.panel_6, wx.ID_ANY, _("puerto"))
        self.lblPort = wx.StaticText(self.panel_6, wx.ID_ANY, _(".."))
        self.sizer_9_staticbox = wx.StaticBox(self.panel_6, wx.ID_ANY, _("puerto"))
        
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.hbtnDTR, self.btnDTR)
        self.Bind(wx.EVT_BUTTON, self.hbtnRTS, self.btnRTS)
        self.Bind(wx.EVT_BUTTON, self.hbtnScriptLoad, self.btnScriptLoad)
        
        self.imgOn = wx.Image("on.png", wx.BITMAP_TYPE_ANY)
        self.imgOff = wx.Image("off.png", wx.BITMAP_TYPE_ANY)
        
        self.ticker = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.ticker)
        self.ticker.Start(250)
        

    def __set_properties(self):
        self.SetTitle(_("control y monitoreo digital"))
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))
        self.label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))
        self.label_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))
        self.label_4.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))
        self.btnDTR.SetMinSize((140, 40))
        self.btnRTS.SetMinSize((140, 40))
        self.lblScriptLoad.SetMinSize((350, 15))
        self.lblScriptLoad.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))
        self.lblScriptPause.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))
        self.lblLogFile.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))
        self.lblLogPause.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))
        self.lblPort.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans [monotype]"))

    def __do_layout(self):       
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_9_staticbox.Lower()
        sizer_9 = wx.StaticBoxSizer(self.sizer_9_staticbox, wx.VERTICAL)
        sizer_14_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_8_staticbox.Lower()
        sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.VERTICAL)
        sizer_14_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_7_staticbox.Lower()
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.VERTICAL)
        sizer_14_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_6_staticbox.Lower()
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.VERTICAL)
        sizer_10_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10_copy = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_5_staticbox.Lower()
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10.Add(self.bmpCD, 0, wx.ALL, 5)
        sizer_10.Add(self.label_1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_5.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_11.Add(self.bmpRI, 0, wx.ALL, 5)
        sizer_11.Add(self.label_2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_5.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_12.Add(self.bmpDSR, 0, wx.ALL, 5)
        sizer_12.Add(self.label_3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_5.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_13.Add(self.bmpCTS, 0, wx.ALL, 5)
        sizer_13.Add(self.label_4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_5.Add(sizer_13, 1, wx.EXPAND, 0)
        self.panel_2.SetSizer(sizer_5)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND, 0)
        sizer_10_copy.Add(self.bmpDTR, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_10_copy.Add(self.btnDTR, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(sizer_10_copy, 1, wx.EXPAND, 0)
        sizer_10_copy_1.Add(self.bmpRTS, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_10_copy_1.Add(self.btnRTS, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(sizer_10_copy_1, 1, wx.EXPAND, 0)
        self.panel_3.SetSizer(sizer_6)
        sizer_3.Add(self.panel_3, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_14.Add(self.btnScriptLoad, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_14.Add(self.lblScriptLoad, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 8)
        sizer_7.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_14_copy.Add(self.btnScriptPause, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_14_copy.Add(self.lblScriptPause, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 8)
        sizer_7.Add(sizer_14_copy, 1, wx.EXPAND, 0)
        self.panel_4.SetSizer(sizer_7)
        sizer_4.Add(self.panel_4, 1, wx.EXPAND, 0)
        sizer_14_copy_1.Add(self.btnLogFile, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_14_copy_1.Add(self.lblLogFile, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 8)
        sizer_8.Add(sizer_14_copy_1, 1, wx.EXPAND, 0)
        sizer_14_copy_2.Add(self.btnLogPause, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_14_copy_2.Add(self.lblLogPause, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 8)
        sizer_8.Add(sizer_14_copy_2, 1, wx.EXPAND, 0)
        self.panel_5.SetSizer(sizer_8)
        sizer_4.Add(self.panel_5, 1, wx.EXPAND, 0)
        sizer_14_copy_3.Add(self.btnPort, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_14_copy_3.Add(self.lblPort, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 8)
        sizer_9.Add(sizer_14_copy_3, 1, wx.EXPAND, 0)
        sizer_9.Add(sizer_14_copy_4, 1, wx.EXPAND, 0)
        self.panel_6.SetSizer(sizer_9)
        sizer_4.Add(self.panel_6, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 2, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()

    def update(self, event):
        self.actualizaEstado(controldig.ser, 1)  
        self.actualizaEstado(controldig.ser, 9)  
        self.actualizaEstado(controldig.ser, 8)  
        self.actualizaEstado(controldig.ser, 6) 

    def hbtnDTR(self, event):  
        """ click botón DTR """
        if controldig.ser.dtr:
            controldig.ser.dtr = 0
            self.bmpDTR.SetBitmap(wx.BitmapFromImage(self.imgOff))
            self.btnDTR.SetLabel("DTR set")
        else:
            controldig.ser.dtr = 1
            self.bmpDTR.SetBitmap(wx.BitmapFromImage(self.imgOn))
            self.btnDTR.SetLabel("DTR reset")               

    def hbtnRTS(self, event):  
        """ click botón RTS """
        if controldig.ser.rts:
            controldig.ser.rts = 0            
            self.bmpRTS.SetBitmap(wx.BitmapFromImage(self.imgOff))
            self.btnRTS.SetLabel("RTS set")
        else:
            controldig.ser.rts = 1            
            self.bmpRTS.SetBitmap(wx.BitmapFromImage(self.imgOn))
            self.btnRTS.SetLabel("RTS reset")
        
        
    def hbtnScriptLoad(self, event):  
        """ click botón Cargar Script 
            actualmente muestra versión
        """        
        self.lblScriptLoad.SetLabel(_("...v.0.1..."))


    def actualizaEstado(self, p, pin):
        """ actualiza bitmaps de cada entrada """
        if pin == 1: # DCD
            if p.cd:
                self.bmpCD.SetBitmap(wx.BitmapFromImage(self.imgOn))
            else:
                self.bmpCD.SetBitmap(wx.BitmapFromImage(self.imgOff))

        if pin == 9: # RI
            if p.ri:
                self.bmpRI.SetBitmap(wx.BitmapFromImage(self.imgOn))
            else:
                self.bmpRI.SetBitmap(wx.BitmapFromImage(self.imgOff))            

        if pin == 8: # CTS
            if p.cts:
                self.bmpCTS.SetBitmap(wx.BitmapFromImage(self.imgOn))
            else:
                self.bmpCTS.SetBitmap(wx.BitmapFromImage(self.imgOff))
                
        if pin == 6: # DSR
            if p.dsr:
                self.bmpDSR.SetBitmap(wx.BitmapFromImage(self.imgOn))
            else:
                self.bmpDSR.SetBitmap(wx.BitmapFromImage(self.imgOff))
     
        if pin == 4: # DTR
            if p.dtr:
                self.bmpDTR.SetBitmap(wx.BitmapFromImage(self.imgOn))
                self.btnDTR.SetLabel("DTR reset") 
            else:
                self.bmpDTR.SetBitmap(wx.BitmapFromImage(self.imgOff))    
                self.btnDTR.SetLabel("DTR set") 

        if pin == 7: # RTS
            if p.rts:
                self.bmpRTS.SetBitmap(wx.BitmapFromImage(self.imgOn))
                self.btnRTS.SetLabel("RTS reset") 
            else:
                self.bmpRTS.SetBitmap(wx.BitmapFromImage(self.imgOff))   
                self.btnRTS.SetLabel("RTS set") 
            
def timeout_scan( s, estados, c, log ):    
    """ callback de timer - se ejecuta cada t_scan """
    global estado_actual
    
    ent = controldig.get_inp_status(s)
        
    entradas_str = controldig.get_inp_status_str(ent)
    e = estados[estado_actual].dar_destino(entradas_str)    
    
    if (e != estado_actual) and (e != -1):
        estado_actual = e
        s.rts = estados[e].rts
        s.dtr = estados[e].dtr
    
    datos = str(estado_actual) + " - " + controldig.reemplazar_nombres(controldig.get_fmt_status(s), c.nombres) 
    #print datos
    
    if c.archivo_registro != "":
        log.guardar_linea([datos,])

# procedimiento que se llama luego de crear GUI
# muy similar a tareas iniiciales de controldig.py
def inicio():
    global estado_actual
    
    estados = {}  
    
    controldig.c = configuracion.Configuracion("controldig.cfg")
    controldig.c.cargar_configuracion()  
   
    try:
        #crea instancia de Serial y abre puerto
        controldig.ser = serial.Serial(controldig.c.puerto, timeout=1) 
    except serial.serialutil.SerialException, mensaje:
        print mensaje
        print "No se puede continuar con la ejecución"
        raise SystemExit
    
    # carga el script para modo automático
    controldig.carga_estados(estados, controldig.c.archivo_estados)
    
    # estado inicial
    try: 
        controldig.salidas = estados[controldig.c.estado_inicial].salidas      
        controldig.ser.dtr = estados[controldig.c.estado_inicial].dtr
        controldig.ser.rts = estados[controldig.c.estado_inicial].rts
        estado_actual = controldig.c.estado_inicial
    except KeyError:
        print "no se especificó un estado inicial"
        estado_actual = 0
        
    if controldig.c.archivo_registro != "":
        controldig.log = registro.Registrador(controldig.c)
    else:
        controldig.log = None
        
    # inicia timer (thread) para obtener estasetdo, procesar script, log etc.
    controldig.tim = timer.tick_timer(controldig.c.t_scan, timeout_scan, [controldig.ser, estados, controldig.c, controldig.log])
    controldig.tim.start()


if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = mainUI(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    
    inicio()

    # fija estado inicial de los indicadores de entradas, botones y labels
    frame_1.actualizaEstado(controldig.ser, 7) 
    frame_1.actualizaEstado(controldig.ser, 4)
    frame_1.lblPort.SetLabel(controldig.c.puerto)
    frame_1.lblLogFile.SetLabel(controldig.c.archivo_registro)
    frame_1.lblScriptLoad.SetLabel(controldig.c.archivo_estados)
    
    app.MainLoop()