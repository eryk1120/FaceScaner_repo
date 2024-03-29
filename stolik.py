#!/usr/bin/env python
# coding=utf-8


import serial
import time

class Table():

    def __init__(self, port='/dev/ttyUSB0', delay=0.01):

        self.inter_delay = delay
        # define serial connection
        self.ser = serial.Serial()
        self.ser.baudrate =9600
        self.ser.port = port
        self.ser.timeout=5
        self.ser.open()

        time.sleep(self.inter_delay)
        self.ser.write(b'\x4c')
        time.sleep(self.inter_delay)
        self.ser.write(b'\xa0')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')

        print(self.ser.read())

    def __del__(self):
        # stop the table just  in case
        self.ser.write(b'\x33')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')

        # close connection
        self.ser.close()

        # cleanup
        del self.ser

    def stop(self):

        time.sleep(self.inter_delay)
        self.ser.write(b'\x33')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')

        print(self.ser.read())
        #print(self.ser.read())
        #print(self.ser.read())


    def rot_letf(self):
        time.sleep(self.inter_delay)
        self.ser.write(b'\xc1')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x09')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')

        temp1 = self.ser.read()
        temp2 = self.ser.read()
        temp3 = self.ser.read()

        if (temp1 == b'xe4' and temp2 == b'xe6'):
            return "DONE"
        else:
            return "something went wrong"

    def rot_right(self):
        time.sleep(self.inter_delay)
        self.ser.write(b'\x81')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x09')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')

        print(self.ser.read())
        print(self.ser.read())
        print(self.ser.read())


    def tick_left(self):
        time.sleep(self.inter_delay)
        self.ser.write(b'\xc1')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x02')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')

        print(self.ser.read())
        print(self.ser.read())
        print(self.ser.read())

    def tick_right(self):
        time.sleep(self.inter_delay)
        self.ser.write(b'\x81')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x02')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')

        print(self.ser.read())
        print(self.ser.read())
        print(self.ser.read())

    def cont_left(self):
        time.sleep(self.inter_delay)
        self.ser.write(b'\xc1')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')
        time.sleep(self.sseemsseemseemsseemsseemsinter_delay)
        self.ser.write(b'\x00')

        print(self.ser.read())


    def cont_right(self):
        time.sleep(self.inter_delay)
        self.ser.write(b'\x81')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')
        time.sleep(self.inter_delay)
        self.ser.write(b'\x00')

        print(self.ser.read())



    def give_stats(self):
        return str(self.ser)

if __name__=='__main__':

    try:
        stolik = Table()

        for i  in range(1):
            #print('LEFT')
            #stolik.rot_letf()
            #print('RIGHT')
            stolik.tick_right()


        #stolik.cont_right()
        #time.sleep(5)
        #stolik.stop()

        del stolik

    except KeyboardInterrupt:
        print('\ntable controller stopped by user interruption\n')
        stolik.stop()
        del stolik
        print('')
    #except:
    #    print('undefined exeption occured')
