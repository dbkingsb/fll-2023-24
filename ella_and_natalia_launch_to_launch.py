from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

leftwheel =  Motor(Port.B,Direction.COUNTERCLOCKWISE)
rightwheel =  Motor (Port.F,Direction.CLOCKWISE)
cat = GyroDriveBase(leftwheel,rightwheel,54,127)
cat.settings(straight_speed=300)
cat.straight(550,Stop.BRAKE)
cat.turn(90)
cat.straight(1080)
cat.curve(300,70)
cat.settings(straight_speed=300)
cat.straight(300)