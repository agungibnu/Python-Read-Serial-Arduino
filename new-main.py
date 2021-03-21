import csv
from datetime import datetime
import serial
import time
#import datetime

comport = 'COM7'
baud    = 9600

openserial = serial.Serial(comport, baud)
#ts = time.time()
#waktu = datetime.datetime.fromtimestamp(ts).strftime("%H%M")


class logger :
    def __init__(self):
        self.data_dict = {}

    def serial_data (self):
        data = openserial.readline().decode('ascii')
        ds = data.split(',')
        self.hm = ds[0]
        self.temp = ds[1]

    def collect_data(self):
        temprature = str(self.temp)
        humidity = str(self.hm)
        self.data_dict['Data Suhu'] = (datetime.now(), humidity, temprature)

    def print_data(self):

        Temperature = str(self.temp)
        Humidity = str(self.hm)
        print("Data Humidity = ", Humidity)
        print("Data Temperature = ", Temperature)

    def logging_data(self):
        for file, data in self.data_dict.items():
            with open('data/' + file + '.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)


def main():
    while True :
        Logger = logger()
        Logger.serial_data()
        Logger.collect_data()
        Logger.logging_data()
        Logger.print_data()
        time.sleep(5)
main()



