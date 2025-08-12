from PiicoDev_VEML6040 import PiicoDev_VEML6040
from machine import Pin
from time import sleep_ms

sensor = PiicoDev_VEML6040()
while True:
    data = sensor.readHSV()
    hue = data['hue']
    label = sensor.classifyHue() 
    print(str(label) + " Hue: " + str(hue))
    sleep_ms(10) #green = 75 -85