from pybricks.parameters import Stop, Port, Direction
from base_robot_Crabby_Cat import BaseRobot
crabby = BaseRobot()
crabby.db.straight(100)
crabby.db.curve(400,-55)
crabby.db.straight(-100)
crabby.db.turn(60)
crabby.db.straight(200)
crabby.db.curve(450,20)