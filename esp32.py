import machine
import time
from machine import Pin, PWM

pin12 = machine.Pin(2, machine.Pin.OUT)
pin0 = machine.Pin(0, machine.Pin.IN)

'''folytkov = True
while folytkov:
    if pin0.value() == 1:
        pin12.value(1)
        
    else:
        pin12.value(0)
        folytkov = False
        vege = "oké"
'''
step = 1
marci = 499
while True:
    pin12.value(1)
    time.sleep_us(marci)
    pin12.value(0)
    time.sleep_us(marci)
    marci += step
    if marci > 500: # 500 
        step = -step
    if marci < 10: # 420,200, 10
        step = -step
  




