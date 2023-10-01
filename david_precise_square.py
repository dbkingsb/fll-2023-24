from base_robot_inventor_bot_m import BaseRobot
from david_utils import play_random_beeps
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop

robot = BaseRobot()
play_random_beeps(robot.hub)
robot.db.settings(300)

for i in range(2):
    robot.db.straight(300)
    robot.db.turn(90)
    robot.db.straight(300)
    robot.db.turn(90)
    robot.db.straight(300)
    robot.db.turn(90)
    robot.db.straight(300)
    robot.db.turn(90)


