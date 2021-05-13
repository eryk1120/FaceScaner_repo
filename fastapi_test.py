from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

import logging as log
log.basicConfig( format='%(levelname)s:  %(asctime)s %(message)s',encoding='utf-8', level=log.INFO,
                    datefmt='%m/%d/%Y %I:%M:%S %p')

import time 


class Head():

    def __init__(self):
        pass

    def __del__(self):
        pass

        

class Message_worker():

    # instrucion procedure for each request
    @staticmethod
    def systemup():
        pass

    @staticmethod
    def systemdown():
        pass

    @staticmethod
    def cameratrigger():
        pass

    @staticmethod
    def chairlefths():
        pass

    @staticmethod
    def chairrighths():
        pass

    @staticmethod
    def chairleftls():
        pass

    @staticmethod
    def movenextpos():
        pass

    @staticmethod
    def movenextposnotrigger():
        pass

    @staticmethod
    def calibratetrigger(params):
        time.sleep(5)

    @staticmethod
    def chairrighths():
        pass

    @staticmethod
    def chairrightls():
        pass

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
        }

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
                self.known_tasks[task](params)
            except Exception as e:
                log.warning( f'failed with task: {task} in sorter.\n Error: {e}')
                
        else:
            try:
                self.known_tasks[task]()
            except Exception as e:
                log.warning( f'failed with task: {task} in sorter.')


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
