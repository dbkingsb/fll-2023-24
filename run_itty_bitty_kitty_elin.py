from base_robot_mr_wiskers_2 import BaseRobot
kitty=BaseRobot()
kitty.db.settings(800, 400, 300, 200)
kitty.db.straight(190)
kitty.db.turn(95)
kitty.db.straight(200)
kitty.db.curve(340,-90)
kitty.db.turn(30)
kitty.db.straight(400)
kitty.db.turn(-30) 
kitty.db.straight(-35)
kitty.frontMotor.run_target(500,75)
kitty.db.turn(180)
kitty.db.turn(45)
kitty.db.straight(250)
kitty.db.turn(-20)
kitty.db.straight(650)
kitty.db.turn(45)
kitty.db.straight(300)



