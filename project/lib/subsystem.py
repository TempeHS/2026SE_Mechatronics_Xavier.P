from time import sleep_ms

class Subsystem:
    def __init__(self, wheels, sensor, usfront, usside, display):
        self.__wheels = wheels
        self.__usfront = usfront
        self.__usside = usside
        self.__sensor = sensor
        self.__display = display
    
    def controller(self):
        distance_front = self.__usfront.distance_mm
        distance_side = self.__usside.distance_mm
        label = self.__sensor.classifyHue()
        if label == "green":
            self.__wheels.stop()
            self.__display.fill(0)
            self.__display.text("green",20,35, 1)
            self.__display.show()
            sleep_ms(1500)
            self.__display.fill(0)
            self.__display.show(0)
            label = "none"
        elif distance_front >= 100:
            self.__wheels.forward_fast()
        else:
            if distance_side < 100:
                self.__wheels.left()
                sleep_ms(900)
                self.__wheels.stop()
            else:
                self.__wheels.right()
                sleep_ms(900)
                self.__wheels.stop()



# scouting


# turning
# check
# retreat 
# stop
#
