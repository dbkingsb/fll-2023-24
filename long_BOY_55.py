from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()
longy = GyroDriveBase(Motor(Port.A), Motor(), wheelDiameter, axleTrack)
longy.straight(500000000)
