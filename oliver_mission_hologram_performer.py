from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

leftwheel =  Motor(Port.B,Direction.COUNTERCLOCKWISE)
rightwheel =  Motor (Port.F,Direction.CLOCKWISE)
cat = GyroDriveBase(leftwheel,rightwheel,54,127)
cat.straight(600)
cat.curve(500,40)
cat.straight(-100)
cat.turn(145)
cat.turn(-10)
cat.straight(800)