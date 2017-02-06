#!/usr/bin/python
# -*- encoding: utf-8 -*-
import time
import serial

def send(data):
   p = serial.Serial("/dev/ttyAMA0" , 57600 )
   p.write(data+"\x0d\x0a")
   data.rstrip()
   print(data)
   time.sleep(2)
   rdata=p.readline()
   rdata=rdata[:-1]
   print rdata

send("sys reset")

time.sleep(1)

send("mac get deveui")
