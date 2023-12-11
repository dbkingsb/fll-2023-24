from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop
blue= BaseRobot()

blue.db.settings(600,400,600,400)

blue.db.curve(150,-97)
blue.db.straight(100)
blue.db.turn(10)
blue.db.straight(900,Stop.NONE)
blue.db.curve(300,76)
blue.db.straight(30)
blue.db.curve(-600,-40)