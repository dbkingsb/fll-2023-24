from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

class BaseRobot:

    def __init__(self):
        self.hub = PrimeHub()
        self.leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.rightMotor = Motor(Port.D, Direction.CLOCKWISE)
        self.topLeftMotor = Motor(Port.F)
        self.wheelDiameter = 55
        self.axleTrack = 129
        self.db = GyroDriveBase(self.leftMotor, self.rightMotor,
            self.wheelDiameter, self.axleTrack)

