from base_robot_mr_wiskers_2 import BaseRobot




brandon_bot= BaseRobot()
brandon_bot.db.settings(800, 800, 100, 200)

brandon_bot.frontMotor.run_target(150,75)
brandon_bot.db.turn(-93)
brandon_bot.frontMotor.run_target(270,5)
brandon_bot.db.straight(50)
brandon_bot.db.straight(200)
brandon_bot.db.straight(-400)
