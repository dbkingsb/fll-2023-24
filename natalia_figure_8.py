from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

leftMotor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.B, Direction.CLOCKWISE)
topLeftMotor = Motor(Port.A)
wheelDiameter = 55
axleTrack = 129
eyes = UltrasonicSensor(Port.D)

#
# Natalia's Figure 8
#

db = GyroDriveBase(leftMotor, rightMotor, wheelDiameter, axleTrack)
db.drive(400,100)
wait (3300)
db.straight(200)
db.drive(400,-100)
wait (3000)
db.straight(250)
db.turn(-40)
db.straight(910)
# db.straight(1900)
