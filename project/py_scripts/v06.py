"""
Read distance from two PiicoDev Ultrasonic Rangefinders independently
"""

from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
import math
from PiicoDev_SSD1306 import *

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 1])  # id argument must match ID switch positions
display = create_PiicoDev_SSD1306()

while True:
    display.fill(0)
    display.text(f"range_a: {range_a.distance_mm}",20,20, 1)
    display.text(f"range_b: {range_b.distance_mm}",20,35, 1)
    display.show()
    print(range_a.distance_mm, range_b.distance_mm)

    sleep_ms(50)
