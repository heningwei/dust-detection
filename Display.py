from pyb import UART
import time
	
class Display():
	def __init__(self,num,value):
		self.uart=UART(num,value)
		time.sleep(1)
	def read_disp(self):
		str='a'
		if self.uart.any()!=0:
			str=self.uart.read()
		if str==b'begin':
			return 3
		elif str==b'end':
			return 1
		else:
			return 0
	def write_disp(self,strr,num):
		a='main.'+strr+'.val='+str(num)
		self.uart.write(a)
		self.uart.writechar(0xff)
		self.uart.writechar(0xff)
		self.uart.writechar(0xff)
		time.sleep(0.03)
	def write_d(self,n0,n1,n2,n3,n4,n5):
		self.write_disp('n0',n0)
		self.write_disp('n1',n1)
		self.write_disp('n2',n2)
		self.write_disp('n3',n3)
		self.write_disp('n4',n4)
		self.write_disp('n5',n5)
