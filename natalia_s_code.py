from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

leftwheel =  Motor(Port.B,Direction.COUNTERCLOCKWISE)
rightwheel =  Motor (Port.F,Direction.CLOCKWISE)
cat = GyroDriveBase(leftwheel,rightwheel,54,127)
cat.drive(400,0)
# cat.drive(400,100)
wait(1300)
cat.curve(250,180)
cat.straight(300)
cat.curve(250,180)
cat.straight(300)