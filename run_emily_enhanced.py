from base_robot_mr_wiskers_2 import BaseRobot
from pybricks.parameters import Stop
blue= BaseRobot()

blue.db.settings(800,600,800,300)

#going to get them
blue.db.straight(200)
blue.db.turn(-60)
blue.db.straight(230)

#Picking them up
blue.db.turn(-74)
blue.db.straight(200)
blue.db.curve(20,50)

#going to dropping them off
blue.db.straight(795,Stop.NONE)

#dropping off emily
blue.db.curve(305,70)
blue.db.straight(-150,Stop.NONE)

#dropping off izzy
blue.db.turn(15)
blue.db.straight(200)
blue.db.turn(30)
blue.db.straight(300)
#going home
blue.db.straight(-800)