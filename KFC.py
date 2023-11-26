from base_robot_mr_wiskers_2 import BaseRobot




brandon_bot= BaseRobot()
brandon_bot.db.settings(turn_rate=100)

# drive to flippy thingy
brandon_bot.frontMotor.run_target(270,75)
brandon_bot.db.straight(230)
brandon_bot.db.turn(-90)
brandon_bot.db.straight(830)
brandon_bot.db.turn(-90)
brandon_bot.db.straight(75)

# flippy thingy move
brandon_bot.frontMotor.run_until_stalled(-270)
brandon_bot.frontMotor.run_target(270,75)
# drive back to home
brandon_bot.db.straight(-50)
brandon_bot.db.turn(-90)
brandon_bot.db.straight(700)
brandon_bot.db.turn(45)
brandon_bot.db.straight(350)

