from time import sleep

class ServoChild:
    # need to integrate v03 code part
    # probably scrap this for pid controller
    def __init__(self, lwheel, rwheel):
        self.__lwheel = lwheel
        self.__rwheel = rwheel
    def forward_slow(self):
        self.__lwheel.set_duty(1662)
        self.__rwheel.set_duty(1300)
    def forward_medium(self):
        self.__lwheel.set_duty(1812)
        self.__rwheel.set_duty(1150)
    def forward_fast(self):
        self.__lwheel.set_duty(1962)
        self.__rwheel.set_duty(1000)
    def back_slow(self):
        self.__lwheel.set_duty(1338)
        self.__rwheel.set_duty(1700)
    def back_medium(self):
        self.__lwheel.set_duty(1188)
        self.__rwheel.set_duty(1850)
    def back_fast(self):
        self.__lwheel.set_duty(1038)
        self.__rwheel.set_duty(2000)
    def stop(self):
        self.__lwheel.set_duty(1500)
        self.__rwheel.set_duty(1500)
    def left(self):
        self.__lwheel.set_duty(1238)
        self.__rwheel.set_duty(1200)
    def right(self):
        self.__lwheel.set_duty(1762)
        self.__rwheel.set_duty(1800)
    
