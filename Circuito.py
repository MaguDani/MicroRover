from microbit import *
from MicroRover import*

rover = Micro_Rover()

while True:
    distancia = rover.get_distance()
    display.show(distancia)
    sensor = rover.infrared_sensor_value()
    if sensor == 2:
        rover.motor(220,220)
    elif sensor == 4:
        rover.motor(0,110)
    elif sensor == 6:
        rover.motor(0,50)
    elif sensor == 1:
        rover.motor(110,0)
    elif sensor == 3:
        rover.motor(50,0)
    elif sensor == 0:
        rover.motor(50,50)
    else:
        rover.motor(255,255)
