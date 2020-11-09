import my_pixtend as px
#from flask import request
import time
import json


class Aparat ():
	'''
	clever description of the class
	'''
	def __init__(self,signal,state, remote):
		self.s = state
		self.i = signal
		self.r = remote
	
	def __del__(self):
		del self.s
		del self.i
		del self.r

	def do_trick(self):
		boo = False
		for i in range(11):
			print_state(self.r)
			time.sleep(1)
			self.r.set(name = self.i,value = not boo )
			boo = not boo
			print_state(self.r)

	def shoot(self):
		self.r.set(name = self.i,value = True )
		time.sleep(0.5)
		self.r.set(name = self.i,value = False )
		time.sleep(0.5)

	def is_ready(self):
		return self.s



class Projector():
	'''
	clever description of the class
	'''
	def __init__(self,signal,state, remote):
		self.s = state
		self.i = signal
		self.r = remote
	
	def __del__(self):
		del self.s
		del self.i
		del self.r

	def ON(self):
		self.r.set(name = self.i,value = True )
	
	def OFF(self):
		self.r.set(name = self.i,value = False )

	def is_ready(self):
		return self.s




class Table():
	'''
	clever description of the class
	'''
	def __init__(self):
		pass
	def __del__(self):
		pass




def print_state(p):
	print("\033c", end="")
	print(p.raport())



class control_center():
	'''
	clever description of the class
	'''

	def __init__(self):
		self.components = {}

	def __init__(self,remote, config):
		self.p = remote
		self.components = {}

		with open("config.json", 'r') as ij:
			temp = json.load(ij)
			for k,v in temp["Components"].items():
				if k.startswith("Cam"):
					print('1: ',k,v)
					self.components[k]= Aparat(remote=self.p,state=v["READY"],signal=v["TRIG"])


				elif k.startswith("Proj"):
					print('2: ',k,v)
					self.components[k]= Projector(remote=self.p,state=v["READY"],signal=v["TRIG"])
	def test(self):
		while (1):
			print("start")
			self.components["Cam0"].shoot()
			time.sleep(0.5)
			self.components["Cam1"].shoot()
			time.sleep(0.5)
			self.components["Cam2"].shoot()
			time.sleep(0.5)
			print("done with cameras!")
			self.components["Proj0"].ON()
			time.sleep(0.5)
			self.components["Proj1"].ON()
			time.sleep(0.5)
			self.p.zero_sys()
			print("done with Projectors")
			time.sleep(2)
			print("DONE!")







if __name__ == "__main__":















	'''
	try:
		p = px.my_pixtend()
		p.zero_sys()

		x = control_center(remote=p,config="config.json")
		x.test()


		p = px.my_pixtend()
		p.zero_sys()

		pr = Projector(remote=p,state="IN0",signal="DO1")
		#a.do_trick()
		print_state(p)
		time.sleep(0.5)
		pr.ON()
		print_state(p)
		time.sleep(5)
		pr.OFF()
		print_state(p)
		time.sleep(0.5)

		print("\033c", end="")
		
		p.zero_sys()

		p.close()
		p = None
		del p
	except KeyboardInterrupt:
		print("\033c", end="")
		print('-'*40,'\n',' '*5,"Program interupted by user! \n",'-'*40)
		p.zero_sys()
		p.close()
		p = None
		del p
'''