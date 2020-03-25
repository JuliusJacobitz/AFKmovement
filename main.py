from pynput.keyboard import Key
from pynput.keyboard import Controller as kcontroller
from pynput.mouse import Controller as mcontroller
from pynput.mouse import Button
import time

from csgoMovement import CSGOMovement as csm

#KeybController = kcontroller()
#MouseController = mcontroller()

def Countdown(secs):
    for i in range(secs):
        time.sleep(1)
        print((secs-i)," seconds left")



Countdown(3)
csm.loop(csm)





"""
except KeyboardInterrupt:
    print("Keyboardinterrupt")
"""