from time import sleep
from machine import Pin, PWM
from servochild import ServoChild
from servo import Servo

lwheel_pwm = PWM(Pin(20))
rwheel_pwm = PWM(Pin(18))

left_wheel = Servo(pwm=lwheel_pwm)
right_wheel = Servo(pwm=rwheel_pwm)

twowheel = ServoChild(left_wheel, right_wheel)

while True:
    twowheel.right()
    sleep(0.9)
    twowheel.stop()
    sleep(4)


