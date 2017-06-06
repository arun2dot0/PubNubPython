#!/usr/bin/env python
from grovepi import *

# Connect the Grove LED to digital port D4
led = 4

pinMode(led,"OUTPUT")

# Turn LED ON
def blink(on_off_num):
    try:
        digitalWrite(led,on_off_num)     # Send HIGH to switch on LED
        if on_off_num == 1:
        	print ("LED ON!")
        else: 	
        	print ("LED OFF!")
    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(led,0)
    return;
