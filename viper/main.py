#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
CL = ColorSensor(Port.S2)
CR = ColorSensor(Port.S3)

ML = Motor(Port.C)
MR = Motor(Port.B)

db = DriveBase(ML, MR, 88, 88)


print('links: ')
print(CL.reflection())
print('rechts: ')
print(CR.reflection())

while True:
    if CR.reflection() < 40:
        db.turn(-2)
    elif CL.reflection() < 40:
        db.turn(2)
    else:
        db.straight(30)
    print('links: ')
    print(CL.reflection())
    print('rechts: ')
    print(CR.reflection())
    wait(10)
            
    