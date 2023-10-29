from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

class BaseRobot:

    def __init__(self):
        self.hub = PrimeHub()
        self.leftMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.rightMotor = Motor(Port.A, Direction.CLOCKWISE)
        self.frontMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.wheelDiameter = 87
        self.axleTrack = 114
        self.db = GyroDriveBase(self.leftMotor, self.rightMotor,
            self.wheelDiameter, self.axleTrack)
