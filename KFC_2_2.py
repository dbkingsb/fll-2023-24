from base_robot_mr_wiskers_2 import BaseRobot




brandon_bot= BaseRobot()
brandon_bot.db.settings(800, 800, 100, 200)

brandon_bot.frontMotor.run_target(270,75)

brandon_bot.db.straight(100)
brandon_bot.frontMotor.run_target(270,25)
brandon_bot.db.straight(-400)
