from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop

bot = BaseRobot()
bot.db.settings(759, 1000, 300, 1000)

# Max East Side Push
# Returns to Launch

bot.frontMotor.run_target(270,-50,wait=False)
bot.db.curve(480,-50)
bot.db.turn(55)
bot.db.straight(70,Stop.NONE)
bot.db.curve(330,20,Stop.NONE)
bot.db.straight(120)
bot.db.turn(53)
bot.db.straight(-600)
bot.db.turn(-50)
bot.db.straight(120)
bot.db.turn(80)
bot.db.straight(400,Stop.NONE)
bot.frontMotor.run_target(270,10,wait=False)
bot.db.curve(400,90)
# bot.db.straight(100)
