from base_robot_mr_wiskers_2 import BaseRobot
blue= BaseRobot()

blue.db.settings(900,900,900,900)

#driving to emily
blue.frontMotor.run_target(400,80)
blue.db.straight(280)
blue.db.turn(-93)

#picking her up
blue.frontMotor.run_target(100,11)
blue.db.straight(255)
blue.db.turn(-38)
blue.db.straight(40)
blue.frontMotor.run_target(270,35)

#Traveling to the popcorn
blue.db.turn(42)
blue.db.straight(980)
blue.db.turn(45)
blue.db.straight(230)

#dropping off
blue.frontMotor.run_target(270,3)
blue.db.straight(-400)
blue.frontMotor.run_target(270,90)

#going home
blue.db.turn(-50)
blue.db.straight(500)