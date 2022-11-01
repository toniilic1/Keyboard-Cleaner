import pynput
from pynput.mouse import Button, Controller


def keyTurnOff(lock_varK):
    if lock_varK == True:
        global keyboard_listener
        keyboard_listener = pynput.keyboard.Listener(suppress=True)
        keyboard_listener.start()
        print('Keyboard locked')
            
                    
def keyTurnOn(lock_varK):
    if lock_varK == False:
        keyboard_listener.stop()
        print('Keyboard unlocked')  



def mouseTurnOff(lock_varM):
    if lock_varM == True:
        global mouse_listener
        mouse_listener = pynput.mouse.Listener(suppress=True)
        mouse_listener.start()
        print('Mouse locked')


def mouseTurnOn(lock_varM):
    if lock_varM == False:
        mouse = Controller()
        mouse_listener.stop()
        mouse.press(Button.left) #fixes the hollow click after activation
        mouse.release(Button.left)
        print('Mouse unlocked')              


class Funcs:
    def key_lock():
        isLocked_K = True
        keyTurnOff(isLocked_K)
        
    def key_unlock():
        isLocked_K = False
        keyTurnOn(isLocked_K)

    def mouse_lock():
        isLocked_M = True
        mouseTurnOff(isLocked_M)

    def mouse_unlock():
        isLocked_M = False
        mouseTurnOn(isLocked_M)