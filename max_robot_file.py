from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

x = Motor(Port.F,Direction.COUNTERCLOCKWISE)
y = Motor(Port.D,Direction.CLOCKWISE)
ruby = GyroDriveBase(x,y,55,130)

ruby.settings(700)
ruby.straight(700,Stop.NONE)
ruby.turn(90,Stop.NONE)
ruby.straight(1400,Stop.NONE)
ruby.turn(90,Stop.NONE)
ruby.straight(700)