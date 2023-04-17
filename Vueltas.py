from microbit import *
from MicroRover import*

rover = Micro_Rover()

while True:
    distancia = rover.get_distance()
    display.show(distancia)
    sensor = rover.infrared_sensor_value()
    if sensor == 2:
        rover.motor(255,255)
    elif sensor == 4:
        rover.motor(0,150)
    elif sensor == 6:
        rover.motor(0,50)
    elif sensor == 1:
        rover.motor(150,0)
    elif sensor == 3:
        rover.motor(50,0)
    else:
        rover.motor(0,0)
