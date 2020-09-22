from pixtendv2l import PiXtendV2L
import time


class my_pixtend(PiXtendV2L):

	DO = {"DO{0}".format(n):n for n in range (0,12,1)}
	RE = {"RE{0}".format(n):n for n in range (0,5,1)}
	IN = {"IN{0}".format(n):n for n in range (0,16,1)}

	def set(self, name , value):
		if type(value) != bool:
			print("required value type is bool")
		if name in self.DO.keys():
			#sterowanie każdym wyjściem na podstawie słowa klucza
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
			#sterowanie każdym przekaźnikiem na podstawie słowa klucza
			if self.RE[name] == 0:
				if value:
					self.relay0 = self.ON
				else:
					self.relay0 = self.OFF
			elif self.RE[name] == 1:
				if value:
					self.relay1 = self.ON
				else:
					self.relay1 = self.OFF
			elif self.RE[name] == 2:
				if value:
					self.relay2 = self.ON
				else:
					self.relay2 = self.OFF
			elif self.RE[name] == 3:
				if value:
					self.relay3 = self.ON
				else:
					self.relay3 = self.OFF
			elif self.RE[name] == 4:
				if value:
					self.relay4 = self.ON
				else:
					self.relay4 = self.OFF
		else:
			print(self.DO[name])
			print("invalid name given")


	def read(self,name):
		"""
		This function reads state of a given input [ "IN{0-15}" ]
		for example if IN0
		"""
		if name in self.IN.keys():
			if self.IN[name] == 0:
				return self.digital_in0
			elif self.IN[name] == 1:
				return self.digital_in1
			elif self.IN[name] == 2:
				return self.digital_in2
			elif self.IN[name] == 3:
				return self.digital_in3
			elif self.IN[name] == 4:
				return self.digital_in4
			elif self.IN[name] == 5:
				return self.digital_in5
			elif self.IN[name] == 6:
				return self.digital_in6
			elif self.IN[name] == 7:
				return self.digital_in7
			elif self.IN[name] == 8:
				return self.digital_in8
			elif self.IN[name] == 9:
				return self.digital_in9
			elif self.IN[name] == 10:
				return self.digital_in10
			elif self.IN[name] == 11:
				return self.digital_in11
			elif self.IN[name] == 12:
				return self.digital_in12
			elif self.IN[name] == 13:
				return self.digital_in13
			elif self.IN[name] == 14:
				return self.digital_in14
			elif self.IN[name] == 15:
				return self.digital_in15
		else:
			pass

	def raport(self):
		str_text = ""
		str_text += " \n"
		str_text += "PiXtend V2 -L- Info:\n"
		str_text += "Firmware:    {0}\n".format(self.firmware)
		str_text += "Hardware:    {0}\n".format(self.hardware)
		str_text += "Model:       {0}\n".format(chr(self.model_in))
		str_text += "-"*20+"\n"
		str_text += "Digital Inputs:\n"
		str_text += "DigitalIn00:  {0}\n".format(self.digital_in0)
		str_text += "DigitalIn01:  {0}\n".format(self.digital_in1)
		str_text += "DigitalIn02:  {0}\n".format(self.digital_in2)
		str_text += "DigitalIn03:  {0}\n".format(self.digital_in3)
		str_text += "DigitalIn04:  {0}\n".format(self.digital_in4)
		str_text += "DigitalIn05:  {0}\n".format(self.digital_in5)
		str_text += "DigitalIn06:  {0}\n".format(self.digital_in6)
		str_text += "DigitalIn07:  {0}\n".format(self.digital_in7)
		str_text += "DigitalIn08:  {0}\n".format(self.digital_in8)
		str_text += "DigitalIn09:  {0}\n".format(self.digital_in9)
		str_text += "DigitalIn10:  {0}\n".format(self.digital_in10)
		str_text += "DigitalIn11:  {0}\n".format(self.digital_in11)
		str_text += "DigitalIn12:  {0}\n".format(self.digital_in12)
		str_text += "DigitalIn13:  {0}\n".format(self.digital_in13)
		str_text += "DigitalIn14:  {0}\n".format(self.digital_in14)
		str_text += "DigitalIn15:  {0}\n".format(self.digital_in15)
		str_text += "-"*20+"\n"
		str_text += "Digital Outputs:\n"
		str_text += "DigitalOut00: {0}\n".format(self.digital_out0)
		str_text += "DigitalOut01: {0}\n".format(self.digital_out1)
		str_text += "DigitalOut02: {0}\n".format(self.digital_out2)
		str_text += "DigitalOut03: {0}\n".format(self.digital_out3)
		str_text += "DigitalOut04: {0}\n".format(self.digital_out4)
		str_text += "DigitalOut05: {0}\n".format(self.digital_out5)
		str_text += "DigitalOut06: {0}\n".format(self.digital_out6)
		str_text += "DigitalOut07: {0}\n".format(self.digital_out7)
		str_text += "DigitalOut08: {0}\n".format(self.digital_out8)
		str_text += "DigitalOut09: {0}\n".format(self.digital_out9)
		str_text += "DigitalOut10: {0}\n".format(self.digital_out10)
		str_text += "DigitalOut11: {0}\n".format(self.digital_out11)
		str_text += "-"*20+"\n"
		str_text += "Relays:\n"
		str_text += "Relay0:      {0}\n".format(self.relay0)
		str_text += "Relay1:      {0}\n".format(self.relay1)
		str_text += "Relay2:      {0}\n".format(self.relay2)
		str_text += "Relay3:      {0}\n".format(self.relay3)
		str_text += "-"*20+"\n"
		return str_text
	def zero_system(self):
		for n in DO.keys():
			self.set(n,False)
		for n in RE.keys():
			self.set(n,False)
	def zero_sys(self):
	    self.digital_out0 = self.OFF
	    self.digital_out1 = self.OFF
	    self.digital_out2 = self.OFF
	    self.digital_out3 = self.OFF
	    self.digital_out4 = self.OFF
	    self.digital_out5 = self.OFF
	    self.digital_out6 = self.OFF
	    self.digital_out7 = self.OFF
	    self.digital_out8 = self.OFF
	    self.digital_out9 = self.OFF
	    self.digital_out10 = self.OFF
	    self.digital_out11 = self.OFF
	    self.relay0 = self.OFF
	    self.relay1 = self.OFF
	    self.relay2 = self.OFF
	    self.relay3 = self.OFF


if __name__ == "__main__":
	p = my_pixtend()

	print("\033c", end="")
	print(p.raport())

	p.set(name="DO0",value=True)

	print("\033c", end="")
	print(p.raport())

	time.sleep(1)
	p.set(name="DO0",value=False)

	print("\033c", end="")
	print(p.raport())

	time.sleep(1)
	p.set(name="DO2",value=True)

	print("\033c", end="")
	print(p.raport())

	time.sleep(1)
	p.set(name="DO2",value=False)

	print(p.raport())
	time.sleep(1)



	p.close()
	p = None
	del p