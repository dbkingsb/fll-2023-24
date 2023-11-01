from base_robot_mr_wiskers_2 import BaseRobot
from david_utils import play_random_beeps
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop, Port, Direction
from pybricks.pupdevices import Motor
import urandom

robot = BaseRobot()

# drive backwards
speed = -300

# start driving
robot.db.drive(speed,0)
driving = True
play_random_beeps(robot.hub)

# the main loop
while True:

    # if we get close to an obstacle 
    if (robot.eyes.distance() < 150):
        driving = False

        # randomly turn left or right
        randomNumber = urandom.randint(0,1)
        robot.db.turn(90 if randomNumber < 1 else -90)
        
        robot.db.drive(speed,0)

    # if we are driving near the desired speed
    if (robot.db.state()[1] < (speed+50)):
        # consider ourselves "driving"
        driving = True

    # if we think we're driving, but our speed is less than we desire
    if (driving == True and robot.db.state()[1] > (speed+50)):

        # consider us no longer driving and turn around
        driving = False
        robot.db.turn(180)
        robot.db.drive(speed,0)

    print(robot.db.state())
    wait(10)
