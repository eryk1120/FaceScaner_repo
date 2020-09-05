from __future__ import print_function
from pixtendv2l import PiXtendV2L
import time
import sys
#from flask_restfull import resource 

class device():
    
    def __init__(self,remote, input, output):
        self.r = remote
        self.i = input
        self.o = output

    def do_work(self):
        print("init")
        if self.i:
            print("at least got here")
            self.o = self.r.ON
            print("output state is: {}".format(self.o))

    

def print_state(p):
    str_text = ""
    # clear the text on screen
    str_text = "                                               \n"
    for i in range(0, 43, 1):
        str_text += "                                               \n"
    str_text += " "
    # Print text to console
    print(str_text, end="\r")
    # Reset cursor
    for i in range(0, 44, 1):
        sys.stdout.write("\x1b[A")  
        
    # Print the info text to console
    str_text += " \n"
    str_text += "PiXtend V2 -L- Info:\n"
    str_text += "Firmware:    {0}\n".format(p.firmware)
    str_text += "Hardware:    {0}\n".format(p.hardware)
    str_text += "Model:       {0}\n".format(chr(p.model_in))
    str_text += " \n"
    str_text += "Digital Inputs:\n"
    str_text += "DigitalIn00:  {0}\n".format(p.digital_in0)
    str_text += "DigitalIn01:  {0}\n".format(p.digital_in1)
    str_text += "DigitalIn02:  {0}\n".format(p.digital_in2)
    str_text += "DigitalIn03:  {0}\n".format(p.digital_in3)
    str_text += "DigitalIn04:  {0}\n".format(p.digital_in4)
    str_text += "DigitalIn05:  {0}\n".format(p.digital_in5)
    str_text += "DigitalIn06:  {0}\n".format(p.digital_in6)
    str_text += "DigitalIn07:  {0}\n".format(p.digital_in7)
    str_text += "DigitalIn08:  {0}\n".format(p.digital_in8)
    str_text += "DigitalIn09:  {0}\n".format(p.digital_in9)
    str_text += "DigitalIn10:  {0}\n".format(p.digital_in10)
    str_text += "DigitalIn11:  {0}\n".format(p.digital_in11)
    str_text += "DigitalIn12:  {0}\n".format(p.digital_in12)
    str_text += "DigitalIn13:  {0}\n".format(p.digital_in13)
    str_text += "DigitalIn14:  {0}\n".format(p.digital_in14)
    str_text += "DigitalIn15:  {0}\n".format(p.digital_in15)
    str_text += " \n"
    str_text += "Digital Outputs:\n"
    str_text += "DigitalOut00: {0}\n".format(p.digital_out0)
    str_text += "DigitalOut01: {0}\n".format(p.digital_out1)
    str_text += "DigitalOut02: {0}\n".format(p.digital_out2)
    str_text += "DigitalOut03: {0}\n".format(p.digital_out3)
    str_text += "DigitalOut04: {0}\n".format(p.digital_out4)
    str_text += "DigitalOut05: {0}\n".format(p.digital_out5)
    str_text += "DigitalOut06: {0}\n".format(p.digital_out6)
    str_text += "DigitalOut07: {0}\n".format(p.digital_out7)
    str_text += "DigitalOut08: {0}\n".format(p.digital_out8)
    str_text += "DigitalOut09: {0}\n".format(p.digital_out9)
    str_text += "DigitalOut10: {0}\n".format(p.digital_out10)
    str_text += "DigitalOut11: {0}\n".format(p.digital_out11)
    str_text += " \n"
    str_text += "Relays:\n"
    str_text += "Relay0:      {0}\n".format(p.relay0)
    str_text += "Relay1:      {0}\n".format(p.relay1)
    str_text += "Relay2:      {0}\n".format(p.relay2)
    str_text += "Relay3:      {0}\n".format(p.relay3)
    str_text += " "
    # Print text to console
    print(str_text, end="\r")
    # Reset cursor
    for i in range(0, 44, 1):
        sys.stdout.write("\x1b[A")

def zero_sys(x):
    x.digital_out0 = x.OFF
    x.digital_out1 = x.OFF
    x.digital_out2 = x.OFF
    x.digital_out3 = x.OFF
    x.digital_out4 = x.OFF
    x.digital_out5 = x.OFF
    x.digital_out6 = x.OFF
    x.digital_out7 = x.OFF
    x.digital_out8 = x.OFF
    x.digital_out9 = x.OFF
    x.digital_out10 = x.OFF
    x.digital_out11 = x.OFF
    x.relay0 = x.OFF
    x.relay1 = x.OFF
    x.relay2 = x.OFF
    x.relay3 = x.OFF

def one_sys(x):
    x.digital_out0 = x.ON
    x.digital_out1 = x.ON
    x.digital_out2 = x.ON
    x.digital_out3 = x.ON
    x.digital_out4 = x.ON
    x.digital_out5 = x.ON
    x.digital_out6 = x.ON
    x.digital_out7 = x.ON
    x.digital_out8 = x.ON
    x.digital_out9 = x.ON
    x.digital_out10 = x.ON
    x.digital_out11 = x.ON
    x.relay0 = x.ON
    x.relay1 = x.ON
    x.relay2 = x.ON
    x.relay3 = x.ON

if __name__ == "__main__":

    #main object to controll
    p = PiXtendV2L()

    if p is not None:
        is_config = False

        while True:
            try:
                # Check if SPI communication is running and the received data is correct
                if p.crc_header_in_error is False and p.crc_data_in_error is False:
                    #init section
                    if not is_config:
                        is_config = True
                        zero_sys(p)
                    # main program 

                    d = device(remote=p , input = p.digital_in1, output = p.digital_out0)
                    d.do_work()
                    



                    # print state of reach pin + additional info
                    #print_state(p)
                # comunication error behavior
                else:
                    for i in range(0, 45, 1):
                        print("")
                    print("")
                    print("Communication error, the data from the microcontroller is not correct!")
                    print("Leaving the application. Please check that the Raspberry Pi can communicate")
                    print("with the microcontroller on the PiXtend V2 -L- board.")
                    print("")
                    
                    p.close()
                    del p
                    p = None
                    break
                    
                # Wait some time, SPI communication will continue in the background
                time.sleep(1)
            # interruption of program behaviour
            except KeyboardInterrupt:
                zero_sys(p)
                p.close()
                del p
                p = None
                print("""
                    --------------------------------------------
                            Process interrupted by user!
                    --------------------------------------------
                    """)
                break
