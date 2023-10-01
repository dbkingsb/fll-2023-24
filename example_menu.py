from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait

menu_options = range(0,9)
menu_index = 0

hub = PrimeHub()
hub.system.set_stop_button(None)

while True:

    hub.display.number(menu_options[menu_index])

    # Wait for any button.
    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(10)
    
    # Wait for the button to be released.
    while hub.buttons.pressed():
        wait(10)

    # Now check which button was pressed.
    if Button.CENTER in pressed:
        # Center button, so the menu is done!
        # Based on the selection, choose a program.
        selected = menu_options[menu_index]
        hub.speaker.play_notes(["C4/16", "G4/16_", "B4/16_", "A4/16"])
        # Now we want to use the Center button as the stop button again.
        # hub.system.set_stop_button(Button.CENTER)
    elif Button.LEFT in pressed:
        # Left button, so decrement menu menu_index.
        menu_index = (menu_index - 1) % len(menu_options)
    elif Button.RIGHT in pressed:
        # Right button, so increment menu menu_index.
        menu_index = (menu_index + 1) % len(menu_options)



