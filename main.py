import time
import serial
import datetime
import time
import csv

comport = 'COM7'
baudrates = 9600
openserial =  serial.Serial(comport, baudrates)
ts = time.time()

data = openserial.readline().decode('ascii')
datasplit = data.split(',')

waktu = datetime.datetime.fromtimestamp(ts).strftime("%H%M")
humidity = datasplit [0]
temperature = datasplit [1]

hum = str(humidity)
temp = str(temperature)

print(humidity)
print(temperature) 


logname = datetime.datetime.fromtimestamp(ts).strftime("%Y%m%d") + ".csv"
#while True :
  
  
    
  







