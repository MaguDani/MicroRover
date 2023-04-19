from microbit import *
from Maqueen import * 

robot = Maqueen()


while True:
    distancia = robot.read_distance()
    if (distancia <= 10):
        robot.set_motor(0,0)
        robot.set_motor(1,0)
    else:
        robot.set_motor(0,255)
        robot.set_motor(1,255)
