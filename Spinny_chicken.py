from base_robot_mr_wiskers_2 import BaseRobot



# 303, 1138, 254, 1145
puffmonster= BaseRobot()
print(puffmonster.db.settings())
puffmonster.db.settings(303, 500, 254, 500)
# puffmonster.db.straight(50)
# puffmonster.db.turn(-44)
# puffmonster.db.straight(430)
puffmonster.db.curve(200,-38)
puffmonster.db.straight(295)
puffmonster.frontMotor.run_time(400,5000)
puffmonster.db.settings(800, 1138, 254, 1145)
puffmonster.db.straight(-400)

