from servo import Servo
from time import sleep

class ServoChild:
    # need to integrate v03 code part
    # probably scrap this for pid controller
    def __init__(self, lwheel, rwheel, debug):
        self.__lwheel = lwheel
        self.__rwheel = rwheel
        self.__debug = debug
    def forward_slow(self):
        self.__lwheel.set_duty(1600)
        self.__rwheel.set_duty(1400)
    def forward_medium(self):
        self.__lwheel.set_duty(2000)
        self.__rwheel.set_duty(1000)
    def forward_fast(self):
        self.__lwheel.set_duty(2500)
        self.__rwheel.set_duty(500)
    def back_slow(self):
        self.__lwheel.set_duty(1400)
        self.__rwheel.set_duty(1600)
    def back_medium(self):
        self.__lwheel.set_duty(1000)
        self.__rwheel.set_duty(2000)
    def back_fast(self):
        self.__lwheel.set_duty(500)
        self.__rwheel.set_duty(2500)
    def stop(self):
        self.__lwheel.set_duty(1500)
        self.__rwheel.set_duty(1500)
    def left(self):
        self.__lwheel.set_duty(1000)
        self.__rwheel.set_duty(1000)
    def right(self):
        self.__lwheel.set_duty(2000)
        self.__rwheel.set_duty(2000)
    
