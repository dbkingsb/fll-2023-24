from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop
blue= BaseRobot()

blue.db.settings(800,600,800,600)

blue.db.straight(200)
blue.db.turn(-60)
blue.db.straight(230)
blue.db.turn(-74)
blue.db.straight(200)
blue.db.curve(20,50)
blue.db.straight(780,Stop.NONE)
blue.db.curve(305,78)
blue.db.straight(-150)
blue.db.turn(15)
blue.db.straight(200)
blue.db.turn(20)
blue.db.straight(300)
blue.db.straight(-800)