import my_pixtend as px
from flask import request
import time



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

	def __init__(self,remote, inf):
		self.p = remote
		self.components = {}





if __name__ == "__main__":
	try:
		'''
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