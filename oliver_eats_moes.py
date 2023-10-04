from base_robot_inventor_bot_m import BaseRobot
from david_utils import play_random_beeps
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop
Moes = BaseRobot()



Moes.db.straight(450)
Moes.db.curve(300,180,wait=False)
Moes.topLeftMotor.run_angle(50,-45,wait=False)
Moes.topRightMotor.run_angle(50,-45,wait=False)
Moes.db.curve(300,180)
Moes.db.straight(150)
Moes.topLeftMotor.run_angle(50,45,wait=False)
Moes.topRightMotor.run_angle(50,45)
Moes.db.straight(-550)



