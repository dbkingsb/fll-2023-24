from base_robot_mr_wiskers_2 import BaseRobot
from david_utils import play_random_beeps
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop

robot = BaseRobot()
play_random_beeps(robot.hub)
robot.db.curve(100,180)
robot.db.curve(100,-360)
robot.db.curve(100,180)
play_random_beeps(robot.hub)


