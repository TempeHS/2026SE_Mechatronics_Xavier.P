from time import sleep_ms

class Controller:
    def __init__(self, wheels, sensor, usfront, usside, display,):
        self.__wheels = wheels
        self.__usfront = usfront
        self.__usside = usside
        self.__sensor = sensor
        self.__display = display
        self.__ongreen = False
    
    def forward_state(self):
        self.__wheels.forward_fast()
    def back_state(self):
        self.__wheels.back_fast()
    def left_state(self):
        self.__wheels.stop()
        sleep_ms(50)
        self.__wheels.left()
        sleep_ms(900)
        self.__wheels.stop()
        sleep_ms(50)
    def right_state(self):
        self.__wheels.stop()
        sleep_ms(50)
        self.__wheels.right()
        sleep_ms(900)
        self.__wheels.stop()
        sleep_ms(50)
    def found_green_state(self):
        self.__wheels.stop()
        self.__display.fill(0)
        self.__display.text("green",20,35, 1)
        self.__display.show()
        sleep_ms(2000)
        self.__display.fill(0)
        self.__display.show()
    def error_state(self):
        self.__display.fill(1)
        self.__display.text("ERROR",20,35, 0)
        self.__display.show()


    def update(self):
        distance_front = self.__usfront.distance_mm
        distance_side = self.__usside.distance_mm
        label = self.__sensor.classifyHue()
        if label == "green" and self.__ongreen == False:
            self.found_green_state()
            self.__ongreen = True
        elif label != "green" and self.__ongreen == True:
            self.__ongreen = False
        if distance_front >= 100:
            self.forward_state()
        else:
            if distance_side < 100:
                self.left_state()
            else:
                self.right_state()




# scouting


# turning
# check
# retreat 
# stop
#
