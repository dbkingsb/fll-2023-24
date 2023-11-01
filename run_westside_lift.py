from base_robot_mr_wiskers_2 import BaseRobot

# Oliver's West Side Lift Missions
# Does NOT yet return to launch
#
Puffball = BaseRobot()
Puffball.frontMotor.run_target(270,75)
Puffball.db.curve(350,-90)
Puffball.frontMotor.run_target(-270,-5)
Puffball.db.turn(180)
Puffball.db.curve(300,-90)
Puffball.frontMotor.run_target(270,75)
Puffball.db.turn(-35)
Puffball.db.straight(30)
Puffball.frontMotor.run_time(-270,1000)
Puffball.db.turn(90)
Puffball.frontMotor.run_target(270,75)
Puffball.db.curve(400,30)
Puffball.db.straight(250)
Puffball.db.turn(-45)
Puffball.frontMotor.run_target(270,0)

