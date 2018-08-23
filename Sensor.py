from pyb import UART
import time

class Sensor():
	def __init__(self,num,value):
		self.data1=0
		self.data2=0
		self.data3=0
		self.data4=0
		self.state=0
		self.uart=UART(num,value)
		time.sleep(1)
	def open_s(self):
		data=[0x11,0x02,0x0b,0x00,0xe2]
		for i in range(0,len(data)):
			self.uart.writechar(data[i])
		time.sleep(0.03)
		while self.uart.any()==0:
			continue
		self.uart.read()
	def close_s(self):
		data=[0x11,0x03,0x0c,0x01,0x1e,0xc1]
		for i in range(0,len(data)):
			self.uart.writechar(data[i])
		time.sleep(0.03)
		while self.uart.any()==0:
			continue
		self.uart.read()
	def work_s(self):
		data=[0x11,0x01,0x0b,0xe3]
		for i in range(0,len(data)):
			self.uart.writechar(data[i])
		time.sleep(0.03)
		while self.uart.any()==0:
			continue
		data_=[]
		for i in range(0,20):
			a=self.uart.readchar()
			if i>=2:
				data_.append(a)
		self.data1=data_[1]*256**3+data_[2]*256**2+data_[3]*256+data_[4]
		self.data2=data_[5]*256**3+data_[6]*256**2+data_[7]*256+data_[8]
		self.data3=data_[9]*256+data_[10]
		self.data4=data_[11]*256+data_[12]
	def read_s(self):
		if self.state==3:
			self.open_s()
			self.state=2
		if self.state==2:
			self.work_s()
		if self.state==1:
			self.close_s()
			self.state=0
		return self.data1,self.data2,self.data3,self.data4
