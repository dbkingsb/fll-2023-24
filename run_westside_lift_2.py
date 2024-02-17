from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop

# Oliver's West Side Lift Missions
# Does NOT yet return to launch
#
Puffball = BaseRobot()
Puffball.db.settings(800, 800, 300, 400)

# Drive To 3D Movie
Puffball.frontMotor.run_target(270,75,wait=False)
Puffball.db.curve(350,-100)

# Do 3D Movie
Puffball.frontMotor.run_target(-270,-36,wait=False)
Puffball.db.turn(195)
Puffball.frontMotor.run_target(270,75,wait=False)

# Drive to Scene Changer
Puffball.db.curve(380,-82)
Puffball.db.turn(-57.5)
# Puffball.db.straight(55)

# Change Scene Orange
Puffball.frontMotor.run_target(270,0,wait=False)
Puffball.db.settings(400, 400, 300, 400)
Puffball.db.straight(185)
Puffball.db.straight(-110)
Puffball.db.straight(115)
Puffball.db.settings(800, 800, 300, 400)
Puffball.db.straight(-175)
# Change Scene 2 Pink
#Puffball.frontMotor.run_target(270,0,wait=False)
# Puffball.db.settings(400, 400, 300, 400)
# Puffball.db.straight(185)
# Puffball.db.settings(800, 800, 300, 400)
# Puffball.db.straight(-175)

# Drive to Immersive Experience
Puffball.frontMotor.run_target(270,75,wait=False)
Puffball.db.turn(90)
Puffball.db.curve(340,45,Stop.NONE)
Puffball.db.straight(180)
Puffball.db.turn(-90)
Puffball.db.straight(55)

# Do Immersive Experience
Puffball.frontMotor.run_time(-150,1100)

# Back to East Home
Puffball.db.straight(-10,Stop.NONE)
Puffball.frontMotor.run_target(270,75,wait=False)
Puffball.db.turn(90)
Puffball.db.straight(450,Stop.NONE)
Puffball.db.curve(400,70,Stop.NONE)
Puffball.db.straight(445,Stop.NONE)
