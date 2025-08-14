from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from subsystem import Subsystem
from servochild import ServoChild
from servo import Servo
from time import sleep_ms
from machine import Pin, PWM
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

lwheel_pwm = PWM(Pin(20))
rwheel_pwm = PWM(Pin(18))

left_wheel = Servo(pwm=lwheel_pwm)
right_wheel = Servo(pwm=rwheel_pwm)

wheels = ServoChild(left_wheel, right_wheel)

sensor = PiicoDev_VEML6040()

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 1])

display = create_PiicoDev_SSD1306()


robot = Subsystem(wheels, sensor, range_a, range_b, display)

while True: 
    robot.controller()
    sleep_ms(50)