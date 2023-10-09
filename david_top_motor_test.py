from base_robot_inventor_bot_m import BaseRobot 
from pybricks.tools import wait, multitask, run_task
from david_utils import play_random_beeps

bot = BaseRobot()

# while True:
#     print("left: " + str(bot.topLeftMotor.angle()) +  ", right: ", str(bot.topRightMotor.angle()))
#     wait(250)

# bot.topLeftMotor.run_target(180, 0, wait=False)
# bot.topRightMotor.run_target(180, 0)
# bot.topLeftMotor.run_target(180, -38, wait=False)
# bot.topRightMotor.run_target(180, -41)

# https://github.com/pybricks/support/issues/917

async def moveLeft():
    await bot.topLeftMotor.run_until_stalled(-180)

async def moveRight():
    await bot.topRightMotor.run_until_stalled(-180)

async def doBoth():
    await multitask(moveLeft(), moveRight())
    bot.topLeftMotor.run_until_stalled(180)
    await bot.topRightMotor.run_until_stalled(180)

run_task(doBoth())
play_random_beeps(bot.hub)


