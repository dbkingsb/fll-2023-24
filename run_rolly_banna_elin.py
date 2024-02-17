from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop
harold = BaseRobot()
harold.db.settings(800, 400, 300, 200)
harold.frontMotor.run_target(300,75,wait=False)

#go to camera
harold.db.straight(70)
harold.db.turn(96)
harold.db.straight(515)

# # move camera
harold.frontMotor.run_until_stalled(-300)
harold.frontMotor.run_target(300,75)
harold.db.straight(-85)
harold.db.turn(-15)
harold.frontMotor.run_until_stalled(-300)


harold.db.straight(-200)
harold.db.curve(300,-35)
harold.frontMotor.run_target(100,75)
harold.db.turn(-65)
harold.db.curve(210,120,Stop.NONE)
harold.db.straight(1300)
# harold.db.turn(-29)
# harold.db.straight(110)
# harold.frontMotor.run_target(270,80,wait=False)


# #go to east home
# harold.db.turn(-65)
# harold.db.curve(200,95,Stop.NONE)
# harold.db.settings(800,1000,400,1000)
# harold.db.straight(1100)
