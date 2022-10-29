import pynput
from pynput.mouse import Button, Controller

class KeyLock:
    def turn_off(lock_varK):
        if lock_varK == True:
            global keyboard_listener
            keyboard_listener = pynput.keyboard.Listener(suppress=True)
            keyboard_listener.start()
            print('Keyboard locked')
            
                    
    def turn_on(lock_varK):
        if lock_varK == False:
            keyboard_listener.stop()
            print('Keyboard unlocked')  


class MouseLock:
    def turn_off(lock_varM):
        if lock_varM == True:
            global mouse_listener
            mouse_listener = pynput.mouse.Listener(suppress=True)
            mouse_listener.start()
            print('Mouse locked')


    def turn_on(lock_varM):
        if lock_varM == False:
            mouse = Controller()
            mouse_listener.stop()
            mouse.press(Button.left) #fixes the hollow click after activation
            mouse.release(Button.left)
            print('Mouse unlocked')              


class Funcs:
    def key_lock():
        isLocked_K = True
        KeyLock.turn_off(isLocked_K)
        
    def key_unlock():
        isLocked_K = False
        KeyLock.turn_on(isLocked_K)

    def mouse_lock():
        isLocked_M = True
        MouseLock.turn_off(isLocked_M)

    def mouse_unlock():
        isLocked_M = False
        MouseLock.turn_on(isLocked_M)