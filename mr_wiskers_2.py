from pybricks.parameters import Stop, Port, Direction
from base_robot_mr_wiskers import BaseRobot
mr = BaseRobot()

# Elin's
mr.frontMoter.run_target(300,70)
mr.db.straight(575)
mr.db.turn(-30)
mr.db.straight(88)
# mr.frontMoter.run_until_stalled(300)
mr.frontMoter.run_time(-300,1000)
mr.frontMoter.run_target(300,-5)
mr.db.turn(50)
mr.db.straight(-109)
mr.frontMoter.run_target(300,70)
mr.db.curve(200,68)
mr.db.settings(straight_speed=600)
mr.db.straight(1000,Stop.NONE)
mr.db.curve(300,90,Stop.NONE)
mr.db.straight(500)

# Natalia's
#
# mr.db.straight(512)
# mr.db.turn(-30)
# mr.db.straight(88)
# mr.frontMoter.run_time(300,1000)
# mr.frontMoter.run_target(300,45)
# mr.db.straight(-100)
# mr.db.turn(90)
# mr.db.straight(100)