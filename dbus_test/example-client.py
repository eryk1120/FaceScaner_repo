#!/usr/bin/env python

import sys
from traceback import print_exc

import dbus

def make_dbus_call(id = None,kill=False,task=None, ping = False):
    bus = dbus.SessionBus()

    if id is not None:
        return
    try:
        remote_object = bus.get_object("com.biometria.HeadService",
                                       "/SomeObject")
                 

        #creating interface 
        iface = dbus.Interface(remote_object, "com.biometria.HeadInterface")

        
        
        # reset daemon
        if kill:
            iface.Exit()

        # send task
        elif task:
            iface.process_task(task)
        

    except dbus.DBusException as e:
        print (e)
        

if __name__ == '__main__':

    head_id = {
    'service': 'com.biometria.HeadService',
    'interface':'com.biometria.HeadInterface'
    }

    make_dbus_call(task={'task':"udało sieeeem"})
