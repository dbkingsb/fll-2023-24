from david_utils import play_random_beeps
from base_robot_mr_wiskers import BaseRobot

bot = BaseRobot()

def exampleBeeps():
    play_random_beeps(bot.hub)

exampleBeeps()