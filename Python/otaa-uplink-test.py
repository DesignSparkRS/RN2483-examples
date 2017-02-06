#!/usr/bin/python
# -*- encoding: utf-8 -*-
import time
import serial

writeconfig=1

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

if writeconfig is 1:
   time.sleep(1)
   send("mac set appeui AAAAAAAAAAAAAAAA")
   send("mac set appkey KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
   send("mac set adr off")
   send("mac save")
   time.sleep(5)

send("mac join otaa")

time.sleep(5)

while True:
   msg="aa"
   send("mac tx uncnf 1 "+msg)
   time.sleep(60)
