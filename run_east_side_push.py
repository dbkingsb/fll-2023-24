from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop

bot = BaseRobot()

# Max East Side Push
# Returns to Launch

bot.frontMotor.run_target(270,70)
bot.db.straight(200)
bot.db.turn(-45)
bot.frontMotor.run_target(270,-7,wait=False)
bot.db.straight(250)
bot.frontMotor.run_target(270,70,wait=False)
bot.db.turn(50)
bot.db.straight(230)
bot.db.turn(37)
bot.frontMotor.run_target(270,-12,wait=False)
bot.db.straight(160)
bot.frontMotor.run_target(270,70,wait=False)
bot.db.straight(-150)
bot.db.turn(-100)
bot.db.straight(200)
bot.db.turn(-56)
bot.db.curve(340,90)
bot.db.turn(97)
bot.frontMotor.run_target(270,-11,wait=False)
bot.db.straight(185)
bot.db.turn(70)
bot.frontMotor.run_target(270,70,wait=False)
bot.db.settings(straight_speed=800)
bot.db.straight(300)
bot.db.turn(-90)
bot.db.straight(240)
bot.db.turn(80)
bot.db.straight(700)