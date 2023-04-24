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


# # Create your objects here.

ev3 = EV3Brick()
ML = Motor(Port.C)
MR = Motor(Port.B)

SL = ColorSensor(Port.S2)
SR = ColorSensor(Port.S3)

schwelle = 30
fehler = 0
pconst = 2
geschwindigkeit = 100

while True:
    fehler = schwelle - SL.reflection()
    MR.run(geschwindigkeit+fehler*pconst)
    ML.run(geschwindigkeit-fehler*pconst)
