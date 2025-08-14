from PiicoDev_VEML6040 import PiicoDev_VEML6040
from machine import Pin
from time import sleep_ms
from PiicoDev_SSD1306 import *

display = create_PiicoDev_SSD1306()

sensor = PiicoDev_VEML6040()

while True:
    data = sensor.readHSV()
    hue = data['hue']
    label = sensor.classifyHue() 
    print(str(label) + " Hue: " + str(hue))
    display.fill(0)
    display.text(f"{str(label)} ",20,20, 1)
    display.text(f"Hue: {str(hue)}",20,35,1)
    display.show()
    sleep_ms(10) #green = 75 -85