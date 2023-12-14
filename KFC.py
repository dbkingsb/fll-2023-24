from base_robot_mr_wiskers_2 import BaseRobot




brandon_bot= BaseRobot()
#(303, 1138, 254, 1145)
brandon_bot.db.settings(800, 300, 300, 400)

# drive to flippy thingy
brandon_bot.frontMotor.run_target(270,75)
brandon_bot.db.straight(230)
brandon_bot.db.turn(-90)
brandon_bot.db.straight(830)
brandon_bot.db.turn(-90)
brandon_bot.db.straight(100)

# flippy thingy move
# brandon_bot.frontMotor.run_until_stalled(-270)
brandon_bot.frontMotor.run_time(-200,1000,wait=False)

# drive back to home

brandon_bot.db.straight(-50)
brandon_bot.frontMotor.run_target(270,75)
brandon_bot.db.turn(-80)
brandon_bot.db.straight(1050)
# brandon_bot.db.turn(45)
# brandon_bot.db.straight(350)

