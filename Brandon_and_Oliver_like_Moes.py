from pybricks.parameters import Stop, Port, Direction
from base_robot_australian_pest_controller import BaseRobot
cheeto_delivery_robot = BaseRobot()
# cheeto_delivery_robot.db.settings(straight_speed=700)
# cheeto_delivery_robot.db.straight(600,Stop.NONE) 
# cheeto_delivery_robot.db.curve(150,90,Stop.NONE)
# cheeto_delivery_robot.db.straight(900,Stop.NONE)
# cheeto_delivery_robot.db.curve(300,90,Stop.NONE)
# cheeto_delivery_robot.db.curve(250,-90)

# Augmented Reality
cheeto_delivery_robot.db.settings(straight_speed=500)
cheeto_delivery_robot.db.straight(600,Stop.NONE) 
cheeto_delivery_robot.db.curve(150,90,Stop.NONE)
cheeto_delivery_robot.db.straight(600,Stop.NONE)
cheeto_delivery_robot.db.turn(-60,Stop.NONE)
cheeto_delivery_robot.db.straight(145)
cheeto_delivery_robot.db.turn(90)
cheeto_delivery_robot.db.straight(350)
cheeto_delivery_robot.db.turn(-45)
cheeto_delivery_robot.db.straight(250)
cheeto_delivery_robot.db.turn(100)
cheeto_delivery_robot.db.straight(250)
cheeto_delivery_robot.db.turn(100)
cheeto_delivery_robot.db.straight(50)
cheeto_delivery_robot.db.straight(-200)
cheeto_delivery_robot.db.turn(-90)
cheeto_delivery_robot.db.straight(200)

# cheeto_delivery_robot.topRightMotor.run_until_stalled(600)


