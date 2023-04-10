from microbit import *
from MicroRover import*

rover = Micro_Rover()

while True:
    distancia = rover.get_distance()
    display.show(distancia)
    if distancia <=15:
        rover.motor(0,0)
        sleep(100)
    else:
        rover.motor(255,255)
        sleep(100)
