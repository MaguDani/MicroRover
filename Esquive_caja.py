from microbit import *
from MicroRover import *

rover = Micro_Rover()

rover.move_forward(4)
rover.girarDerecha()
rover.move_forward(2)
rover.girarIzquierda()
rover.move_forward(3)
rover.girarIzquierda()
rover.move_forward(3)
rover.girarDerecha()
rover.move_forward(2)
