from base_robot_mr_wiskers_2 import BaseRobot

bot = BaseRobot()

# Max East Side Push
# Returns to Launch
#
bot.frontMotor.run_target(270,70)
bot.db.straight(200)
bot.db.turn(-45)
bot.frontMotor.run_target(270,-7,wait=False)
bot.db.straight(250)
bot.frontMotor.run_target(270,70)
bot.db.turn(50)
bot.db.straight(220)
bot.db.turn(37)
bot.frontMotor.run_target(270,-7,wait=False)
bot.db.straight(160)
bot.db.straight(-150)
bot.db.turn(-100)
bot.db.straight(540)
bot.db.turn(180)
bot.db.straight(600)
bot.db.turn(40)
bot.db.straight(400)