from base_robot_mr_wiskers_2 import BaseRobot
kitty=BaseRobot()
kitty.db.straight(190)
kitty.db.turn(95)
kitty.db.straight(200)
kitty.db.curve(350,-90)
kitty.db.turn(30)
kitty.db.straight(340) 
kitty.frontMotor.run_target(270,65)
kitty.db.turn(-120)
kitty.db.straight(550)
kitty.db.turn(-85)
kitty.db.straight(700)

