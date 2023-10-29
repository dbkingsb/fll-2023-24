from base_robot_mr_wiskers_2 import BaseRobot

bot = BaseRobot()

# wave hi
bot.frontMotor.run_target(270,70)
bot.frontMotor.run_target(270,0)
bot.frontMotor.run_target(270,70)
bot.frontMotor.run_target(270,0)
