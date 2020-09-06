from pixtendv2l import PiXtendV2L
import time


class my_pixtend(PiXtendV2L):

	DO = {"DO{0}".format(n):n for n in range (0,12,1)}
	RE = {"RE{0}".format(n):n for n in range (0,5,1)}
	IN = {"IN{0}".format(n):n for n in range (0,16,1)}

	def set(self, name , value):
		print("====================\nname: {0}\nvalue: {1}\n--------------------".format(name,value))
		if type(value) != bool:
			print("required value type is bool")
		if name in self.DO.keys():

			if self.DO[name] == 0:
				if value:
					self.digital_out0 = self.ON
				else:
					self.digital_out0 = self.OFF
			elif self.DO[name] == 1:
				if value:
					self.digital_out1 = self.ON
				else:
					self.digital_out1 = self.OFF
			elif self.DO[name] == 2:
				if value:
					self.digital_out2 = self.ON
				else:
					self.digital_out2 = self.OFF
			elif self.DO[name] == 3:
				if value:
					self.digital_out3 = self.ON
				else:
					self.digital_out3 = self.OFF
			elif self.DO[name] == 4:
				if value:
					self.digital_out4 = self.ON
				else:
					self.digital_out4 = self.OFF
			elif self.DO[name] == 5:
				if value:
					self.digital_out5 = self.ON
				else:
					self.digital_out5 = self.OFF
			elif self.DO[name] == 6:
				if value:
					self.digital_out6 = self.ON
				else:
					self.digital_out6 = self.OFF
			elif self.DO[name] == 7:
				if value:
					self.digital_out7 = self.ON
				else:
					self.digital_out7 = self.OFF
			elif self.DO[name] == 8:
				if value:
					self.digital_out8 = self.ON
				else:
					self.digital_out8 = self.OFF
			elif self.DO[name] == 9:
				if value:
					self.digital_out9 = self.ON
				else:
					self.digital_out9 = self.OFF
			elif self.DO[name] == 10:
				if value:
					self.digital_out10 = self.ON
				else:
					self.digital_out10 = self.OFF
			elif self.DO[name] == 11:
				if value:
					self.digital_out11 = self.ON
				else:
					self.digital_out11 = self.OFF
			else:
				print("smth went wrong\nvalue = {0}".format(value))
		elif name in self.RE.keys():
			pass
		else:
			print(self.DO[name])
			print("invalid name given")


	def read(self):
		pass









p = my_pixtend()

p.set(name="DO0",value=True)
time.sleep(1)
p.set(name="DO0",value=False)
time.sleep(1)
p.set(name="DO2",value=True)
time.sleep(1)
p.set(name="DO2",value=False)
time.sleep(1)

p.close()
p = None
del p