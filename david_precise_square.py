from base_robot_mr_wiskers_2 import BaseRobot
from david_utils import play_random_beeps
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop

robot = BaseRobot()
play_random_beeps(robot.hub)
robot.db.settings(straight_speed=200,turn_rate=90)

for i in range(20):
    # robot.frontMotor.run_target(100,0)
    robot.db.straight(300)
    robot.db.turn(90)
    # robot.frontMotor.run_target(270,70)
    # robot.frontMotor.run_time(-270, 1000)


