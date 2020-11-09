import RPi.GPIO as GPIO
import json

class Controler():
    """docstring for ClassName"""
    def __init__(self,config_json):

        GPIO.setmode(GPIO.BCM)

        with open("config.json", 'r') as ij:
            temp = json.load(ij)
            self.components=temp["Components"]
        print (self.components)
        for k1,v1 in self.components.items():
            for k2,v2 in v1.items():

                print(k2,": ",v2)

                if k2.startswith("IN_"):
                    GPIO.setup(v2,GPIO.OUT)
                elif k2.startswith("OUT_"):
                    GPIO.setup(v2,GPIO.IN)





    def __del__(self):
        del self.components

if __name__=="__main__":
    x = Controler("config.json")
    GPIO.cleanup()




"""
            for k,v in temp["Components"].items():
                if k.startswith("Cam"):
                    print('1: ',k,v)
                    self.components[k]= {"READY":v["READY"],"TRIG":v["TRIG"]}


                elif k.startswith("Proj"):
                    print('2: ',k,v)
                    self.components[k]= {"READY":v["READY"],"TRIG":v["TRIG"],"ACTIVE":v["ACTIVE"]}
"""