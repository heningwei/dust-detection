# main.py -- put your code here!
#from pyb import UART
#from pyb import Pin
from pyb import LED
from Dht11 import Dht11
from Sensor import Sensor
from Display import Display

sensor=Sensor(4,9600)
display=Display(6,9600)
dht11=Dht11('X7')

l1=LED(1)
l2=LED(2)
l3=LED(3)
l4=LED(4)

cnt=10
n4=0
n5=0

while True:
	a=display.read_disp()
	l1.toggle()
	if a!=0:
		sensor.state=a
	n0,n1,n2,n3=sensor.read_s()
	l2.toggle()
	cnt=cnt-1
	if cnt==0:
		n4,n5=dht11.read_temps()
		cnt=10
#	n4,n5=25,50
	l3.toggle()
	display.write_d(n0,n1,n2,n3,n4,n5)
	l4.toggle()
