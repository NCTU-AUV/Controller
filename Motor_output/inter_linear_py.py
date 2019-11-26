import serial
from time import sleep
#from pylab import plt
#import numpy as np

x = [
    -9,
    -8.9,
    -8.7,
    -8.44,
    -8.23,
    -7.98,
    -7.59,
    -7.28,
    -7.02,
    -6.74,
    -6.41,
    -6.21,
    -5.97,
    -5.57,
    -5.21,
    -4.98,
    -4.8,
    -4.39,
    -4.15,
    -3.9,
    -3.62,
    -3.29,
    -2.94,
    -2.74,
    -2.47,
    -2.26,
    -2,
    -1.74,
    -1.53,
    -1.36,
    -1.15,
    -0.96,
    -0.78,
    -0.61,
    -0.42,
    -0.25,
    -0.12,
    -0.06,
    0,
    0.13,
    0.25,
    0.41,
    0.58,
    0.77,
    0.92,
    1.15,
    1.4,
    1.58,
    1.86,
    2.08,
    2.43,
    2.75,
    3.07,
    3.37,
    3.7,
    3.98,
    4.32,
    4.62,
    4.89,
    5.32,
    5.56,
    5.94,
    6.23,
    6.66,
    7.04,
    7.39,
    7.6,
    7.7,
    8.33,
    8.69,
    8.83,
    9.25,
    9.65,
    10.07,
    10.59,
    10.8,
    11.23,
]

y = [
    1100,
    1110,
    1120,
    1130,
    1140,
    1150,
    1160,
    1170,
    1180,
    1190,
    1200,
    1210,
    1220,
    1230,
    1240,
    1250,
    1260,
    1270,
    1280,
    1290,
    1300,
    1310,
    1320,
    1330,
    1340,
    1350,
    1360,
    1370,
    1380,
    1390,
    1400,
    1410,
    1420,
    1430,
    1440,
    1450,
    1460,
    1470,
    1500,
    1530,
    1540,
    1550,
    1560,
    1570,
    1580,
    1590,
    1600,
    1610,
    1620,
    1630,
    1640,
    1650,
    1660,
    1670,
    1680,
    1690,
    1700,
    1710,
    1720,
    1730,
    1740,
    1750,
    1760,
    1770,
    1780,
    1790,
    1800,
    1810,
    1820,
    1830,
    1840,
    1850,
    1860,
    1870,
    1880,
    1890,
    1900,
]

def binSearch(arr, l, r, x):
    if x < arr[l]:
        return -1
    elif x > arr[r]:
        return -2
    
    while r-l+1 > 2:
        m = (l+r)//2
        if arr[m] <= x:
            l = m
        else:
            r = m - 1
    
    for i in range(r, l-1, -1):
        if arr[i] <= x:
            return i
        

def interpolation(a):
    index = binSearch(x, 0, len(x)-1, a)
    
    if index == -1:
        return (y[1] - y[0]) / (x[1] - x[0]) * (a - x[0] + y[0])
    if index == -2:
        return (y[len(x)-1] - y[len(x)-2]) / (x[len(x)-1] - x[len(x)-2]) * (a - x[len(x)-2]) + y[len(x)-2]
    return (y[index+1] - y[index]) / (x[index+1] - x[index]) * (a - x[index]) + y[index]


if __name__ == '__main__':
    
    COM_PORT = '/dev/ttyACM0'   
    BAUD_RATES = 115200    
    arduino = serial.Serial(COM_PORT, BAUD_RATES)   
    # string = arduino.readline()
    
    #arduino.flush()
    for i in range(100):
        input_data = [7565, 7566, 7667, 7668, 7769, 7770, 7871, 7872]
        
        output_data_num = []
        #output_data_num

        #output_data_num.append(int())
        for j in range(8):
            output_data_num.append(int(input_data[j]//100))
            output_data_num.append(int(input_data[j]%100))
        
        #print(bytearray(output_data_num))
        arduino.write(bytearray(output_data_num))
        print(arduino.readline())

        sleep(0.01)
        
    
    arduino.flush()
    arduino.close()
    
    print("End.")
        
        
