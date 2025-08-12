from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from servochild import ServoChild
from time import sleep_ms

class Subsystem:
    def __init__(self, lwheel, rwheel, sensor, usfront, usside):
        self.__wheels = ServoChild(lwheel, rwheel)
        self.__usfront = usfront
        self.__usside = usside
        self.__sensor = sensor
    
    def controller(self):
        distance_front = self.__usfront.distance_mm
        distance_side = self.__usside.distance_mm
        if distance_front >= 250:
            self.__wheels.forward_medium()
        elif distance_front >= 150:
            self.__wheels.forward_slow()
        elif distance_front >= 100:
            if distance_side < 100:
                self.__wheels.left()
        else:
            self.__wheels.back_medium()


# scouting


# turning
# check
# retreat 
# stop
#
