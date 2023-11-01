from base_robot_mr_wiskers_2 import BaseRobot
from david_utils import play_random_beeps
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop

robot = BaseRobot()
play_random_beeps(robot.hub)
print(robot.db.settings())
robot.db.settings(800, 600, 254, 600)

for i in range(10):
    robot.db.straight(3000)
    robot.db.turn(180)
    # robot.db.curve(300,360,Stop.NONE)


