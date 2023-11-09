from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop

# Oliver's West Side Lift Missions
# Does NOT yet return to launch
#
Puffball = BaseRobot()
Puffball.db.settings(800, 400, 300, 200)

# Drive To 3D Movie
Puffball.frontMotor.run_target(270,75)
Puffball.db.curve(345,-95)

# Do 3D Movie
Puffball.frontMotor.run_target(-270,-5)
Puffball.db.turn(185)
Puffball.frontMotor.run_target(270,75)

# Drive to Scene Changer
Puffball.db.curve(375,-82)
Puffball.db.turn(-50)
Puffball.db.straight(55)

# Change Scene
Puffball.frontMotor.run_time(-270,1000)
Puffball.frontMotor.run_target(270,75)

# Drive to Immersive Experience
Puffball.db.straight(-55)
Puffball.db.turn(90)
Puffball.db.curve(340,45,Stop.COAST_SMART)
Puffball.db.straight(180)
Puffball.db.turn(-90)
Puffball.db.straight(35)

# Do Immersive Experience
Puffball.frontMotor.run_time(-90,1100)
Puffball.frontMotor.run_target(270,75)

# Back to East Home
Puffball.db.straight(-10,Stop.NONE)
Puffball.db.turn(90)
Puffball.db.straight(550,Stop.NONE)
Puffball.db.curve(400,90,Stop.NONE)
Puffball.db.straight(400)
