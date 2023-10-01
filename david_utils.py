from pybricks.hubs import PrimeHub
import urandom

def play_random_beeps(hub:PrimeHub):
    for i in range(3):
        x = urandom.randint(50,1000)
        hub.speaker.beep(x)
