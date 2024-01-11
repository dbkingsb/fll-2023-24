from base_robot_mr_wiskers_2 import BaseRobot



# 303, 1138, 254, 1145
puffmonster= BaseRobot()
print(puffmonster.db.settings())
puffmonster.db.straight(100)
puffmonster.db.turn(-47)
puffmonster.db.straight(399)
puffmonster.frontMotor.run_time(400,5000)
puffmonster.db.settings(800, 1138, 254, 1145)
puffmonster.db.straight(-400)

