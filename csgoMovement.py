from pynput.keyboard import Key
from pynput.keyboard import Controller as kcontroller
from pynput.mouse import Controller as mcontroller
from pynput.mouse import Button
import time

KeybController = kcontroller()
MouseController = mcontroller()

class CSGOMovement():
    def __init__(self):
        pass

    def forward(self):
        KeybController.press(Key.space)
        time.sleep(2)
        KeybController.release(Key.space)

    def backward(self):
        KeybController.press('s')
        time.sleep(2)
        KeybController.release('s')

    def straveLeft(self):
        KeybController.press('a')
        time.sleep(2)
        KeybController.release('a')

    def straveRight(self):
        KeybController.press('d')
        time.sleep(2)
        KeybController.release('d')


    def afkKey(self):
        self.forward(self)
        self.backward(self)
        self.straveLeft(self)
        self.straveRight(self)

        self.backward(self)
        self.forward(self)
        self.straveRight(self)
        self.straveLeft(self)

    def afkMouse(self):
        MouseController.move(10,0)
        time.sleep(0.25)

    def loop(self, times = 0):

        if times < 1:
            try:
                while True:
                    self.afkMouse(self)
                    self.afkKey(self)       # wenn fehler dann hier
                    #time.sleep(2)

            except KeyboardInterrupt:
                print("interrupted")

        else:
            try:
                for i in range(times):
                    #self.afkKey(self)
                    self.afkMouse(self)
                    #time.sleep(2)

            except KeyboardInterrupt:
                print("interrupted")



