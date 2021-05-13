from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

import logging as log
log.basicConfig( format='%(levelname)s:  %(asctime)s %(message)s',encoding='utf-8', level=log.INFO,
                    datefmt='%m/%d/%Y %I:%M:%S %p')

import time 

import sys
from traceback import print_exc

import dbus


class Head():

    def __init__(self):
        pass

    def __del__(self):
        pass

head_id = {
    'service': 'com.biometria.HeadService',
    'interface':'com.biometria.HeadInterface'
}

class Message_worker():

    def __init__(self):
        self.known_tasks = {
            "systemup":self.systemup,
            "systemdown":self.systemdown,
            "cameratrigger":self.cameratrigger,
            "chairlefths":self.chairlefths,
            "chairleftls":self.chairleftls,
            "chairrighths":self.chairrighths,
            "chairrightls":self.chairrightls,
            "calibratetrigger":self.calibratetrigger,
            "movenextpos":self.movenextpos,
            "movenextposnotrigger":self.movenextposnotrigger,
            "reset_system":self.reset_system
        }

    @staticmethod
    def make_dbus_call(id = None,kill=False,task=None, ping = False):

        '''
        that funciton calls another process via dbus
        '''

        bus = dbus.SessionBus()

        if id is None:
            return
        try:
            remote_object = bus.get_object(id['service'],
                                        "/SomeObject")
                    

            #creating interface 
            iface = dbus.Interface(remote_object, id['interface'])

            
            
            # reset daemon
            if kill:
                iface.Exit()

            # send task
            elif task:
                iface.process_task(task)
            

        except dbus.DBusException as e:
            print (e)

    # instrucion procedure for each request

    # podnośniki 
    def systemup(self):
        pass

    def systemdown(self):
        pass

    # stolik obrotowy
    def chairlefths(self):
        pass

    def chairrighths(self):
        pass

    def chairrightls(self):
        pass

    def chairleftls(self):
        pass
    
    # komendy do głowicy
    def cameratrigger(self):
        self.make_dbus_call(id = head_id,task={'task':'camera_trigger'})

    def calibratetrigger(self,params):
        self.make_dbus_call(id = head_id,task={'task':'calibrate',
                                                'projektor':str(params['param_a']),
                                                'kamera':str(params['param_b'])})

    def movenextpos():
        self.calibratetrigger()
        #ruch stolika o 15 stopni
        self.chairrighths()

    def movenextposnotrigger():
        self.chairrighths()

    def reset_system():
        pass

    

    def __del__(self):
        del self.tasks

    def sorter(self, task = str,params = None):

        f'''
        Method used for sorting request data and passing it forward.
        takes 1 required  str argument "task" and one optional dictionary 

        List of supported tasks:
        {self.known_tasks.keys()}

        Only 'calibratetrigger' utilizes given dict.
        '''


        if task == "calibratetrigger":
            try:
                self.known_tasks[task](params=params)
            except Exception as e:
                log.warning( f'failed with task: {task} in sorter.\n Error: {e}')
                
        else:
            try:
                self.known_tasks[task]()
            except Exception as e:
                log.warning( f'failed with task: {task} in sorter.')
                log.warning(e)


# declaration of objets 

message_worker = Message_worker()

# api 'data'  class
class Hardware_interface(BaseModel):
    message: str
    ctrl_param_a: Optional[int] = None
    ctrl_param_b: Optional[int] = None

app = FastAPI()

# post request handler 
@app.post("/items/")
async def create_item(item: Hardware_interface):
    try:
        task = item.message
        params = {"param_a":item.ctrl_param_a,'param_b':item.ctrl_param_b}
        log.info(f'aquired request on: {task} with parameters: {params}' )
        message_worker.sorter(task=task,params=params)
        return item
    except Exception as e:
        log.Error(f"FAILED WHILE PARSING REQUEST:{item}")
        return 300


