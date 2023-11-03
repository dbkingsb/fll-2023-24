from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop

bot = BaseRobot()

# Max East Side Push
# Returns to Launch
#
bot.frontMotor.run_target(270,70)
bot.db.straight(200)
bot.db.turn(-45)
bot.frontMotor.run_target(270,-7,wait=False)
bot.db.straight(250)
bot.frontMotor.run_target(270,70,wait=False)
bot.db.turn(50)
bot.db.straight(220)
bot.db.turn(37)
bot.frontMotor.run_target(270,-12,wait=False)
bot.db.straight(160)
bot.frontMotor.run_target(270,70,wait=False)
bot.db.straight(-150)
bot.db.turn(-100)
bot.db.straight(520)
bot.frontMotor.run_target(270,-12)
bot.db.turn(180)
bot.frontMotor.run_target(270,70,wait=False)
bot.db.settings(straight_speed=800)
bot.db.straight(600)
bot.db.turn(40)
bot.db.straight(550)