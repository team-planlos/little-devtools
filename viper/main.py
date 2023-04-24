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

while True:
    if CL.reflection() < 50:
        db.straight(30)
        if CL.reflection<50 and CR.reflection<50:
            db.turn(60)
        elif CR.reflection()>50:
            db.turn(300)
        else:
            db.straight(50)
    db.straight(50)
            
    