
from microbit import *
from MicroRover import *

rover = Micro_Rover()
while True:

    distancia = rover.get_distance()
    display.show(distancia)
    
    if distancia < 35:
        rover.motor(-255,-255)
        sleep(100)
        rover.motor(0,-255)
        
    else:
        rover.motor(255,255)
        sleep(100)
