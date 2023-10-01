from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

class BaseRobot:

    def __init__(self):
        self.hub = PrimeHub()
        self.leftMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.rightMotor = Motor(Port.F, Direction.CLOCKWISE)
        self.topLeftMotor = Motor(Port.C)
        self.wheelDiameter = 56
        self.axleTrack = 129
        self.eyes = UltrasonicSensor(Port.D)
        self.db = GyroDriveBase(self.leftMotor, self.rightMotor,
            self.wheelDiameter, self.axleTrack)

