from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop
kitty=BaseRobot()
# Going to museum 
kitty.db.settings(800, 400, 300, 200)
kitty.db.curve(200,85)
kitty.db.straight(200)
kitty.db.curve(220,-55)
kitty.db.straight(590)
kitty.db.straight(-500,Stop.NONE)
kitty.db.curve(-500,-85)

