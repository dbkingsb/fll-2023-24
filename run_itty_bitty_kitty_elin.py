from base_robot_mr_wiskers_2 import BaseRobot
kitty=BaseRobot()
kitty.db.straight(200)
kitty.db.turn(95)
kitty.db.straight(200)
kitty.db.curve(350,-90)
kitty.db.turn(25)
kitty.db.straight(325) 
kitty.frontMotor.run_target(270,75)


