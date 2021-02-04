import RPi.GPIO as GPIO
import json
import time

class Controler():
    """docstring for ClassName"""
    def __init__(self,config_json):

        GPIO.setmode(GPIO.BOARD)

        with open("config.json", 'r') as ij:
            temp = json.load(ij)
            self.components=temp["Components"]
        print (self.components)
        for _,v1 in self.components.items():
            for k2,v2 in v1.items():

                print(k2,": ",v2)

                if k2.startswith("IN_"):
                    GPIO.setup(v2,GPIO.OUT)
                elif k2.startswith("OUT_"):
                    GPIO.setup(v2,GPIO.IN)
    def test(self):
        """
        docstring
        """
        # napraw to eryku z przyszłości
        print("HIGH",self.components["Cam0"]["IN_TRIG"],type(self.components["Cam0"]["IN_TRIG"]))
        GPIO.output(self.components["Cam0"]["IN_TRIG"],GPIO.HIGH)
        time.sleep(10)
        print("LOW",self.components["Cam0"]["IN_TRIG"],type(self.components["Cam0"]["IN_TRIG"]))
        GPIO.output(self.components["Cam0"]["IN_TRIG"],GPIO.LOW)
        time.sleep(10)
        GPIO.wait_for_edge(self.components["Proj0"]['OUT_ACTIVE'], GPIO.RISING) # we wait for the button to be pressed
		GPIO.output(self.components["Cam0"]['IN_TRIG'], GPIO.HIGH)
		GPIO.output(self.components["Cam0"]['IN_TRIG'], GPIO.LOW)



    def __del__(self):
        del self.components
        GPIO.cleanup()

if __name__=="__main__":
    x = Controler("config.json")
    x.test()
    del x
