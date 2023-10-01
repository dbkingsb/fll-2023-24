from pybricks.parameters import Stop, Port, Direction
from base_robot_inventor_bot_m import BaseRobot
cheeto_delivery_robot = BaseRobot()
cheeto_delivery_robot.db.settings(straight_speed=700)
cheeto_delivery_robot.db.straight(600,Stop.NONE) 
cheeto_delivery_robot.db.curve(150,90,Stop.NONE)
cheeto_delivery_robot.db.straight(900,Stop.NONE)
cheeto_delivery_robot.db.curve(300,90,Stop.NONE)
cheeto_delivery_robot.db.curve(250,-90)