import bluetooth
import time
import csv
import threading

#Local imports
from bt import *
from plotter import *

test_mode = False

#Bluetooth ports used for the data threads
portRight = 9
portFront = 10
portBack  = 11

#path to the sensor data folder
path_csv = "C:\\Users\\Mihai\\Desktop\\Master_thesis\\Sensor_data\\"

#select proper .csv files depending on the running mode 
if test_mode == False:
    print ("Normal mode selected")
    right_sensor_file = "right_distance.csv" 
    front_sensor_file = "front_distance.csv" 
    back_sensor_file  = "back_distance.csv"  
else:
    print ("Test mode selected")
    right_sensor_file = "test_right_distance.csv" 
    front_sensor_file = "test_front_distance.csv" 
    back_sensor_file  = "test_back_distance.csv"

#select proper .csv files depending on the running mode 
full_path_right = path_csv + right_sensor_file
full_path_front = path_csv + front_sensor_file
full_path_back  = path_csv + back_sensor_file

print ("[CSV] Front thread writing to file :", full_path_front)
print ("[CSV] Right thread writing to file :", full_path_right)
print ("[CSV] Back  thread writing to file :", full_path_back)

#if running mode is selected start data acquisition threads
if test_mode == False:

    print ("Starting data acquisition threads")

    rightThread = threading.Thread(target=dataThread, args=('right', portRight, full_path_right))    
    rightThread.start()

    frontThread = threading.Thread(target=dataThread, args=('front', portFront, full_path_front))    
    frontThread.start()

    backThread = threading.Thread(target=dataThread, args=('back', portBack, full_path_back))    
    backThread.start()

#call the plotting function using the 3 .csv files generated by the data threads
plotMain(file_path_front = full_path_front, file_path_right = full_path_right, file_path_back=full_path_back) 

