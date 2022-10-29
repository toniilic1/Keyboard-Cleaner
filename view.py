import tkinter as tk
from controllers import Funcs

def main():

    root = tk.Tk()
    root.minsize(300, 200)
    root.title('K&B Cleaner')
    root.resizable(False, False)
    root.iconbitmap('images/flavicon.ico')

    keyLabel = tk.Label(root, text = "Keyboard", font = ('Helvetica', 24))
    keyLabel.grid(column = 0, row = 0, padx = 30)
    textLabel = tk.Label(root, text = "", font = ('Helvetica'))
    textLabel.grid(column = 0, row = 1, sticky = 'n')

    mouseLabel = tk.Label(root, text = "Mouse", font = ('Helvetica', 24))
    mouseLabel.grid(column = 0, row = 2, padx = 30)
    text2Label = tk.Label(root, text = "", font = ('Helvetica'))
    text2Label.grid(column = 0, row = 3, sticky = 'n')

    def key_switch():
        global is_onK

        if is_onK:
            key_button.config(image = off)
            textLabel.config(text = "Keyboard is unlocked", fg = "grey")
            Funcs.key_unlock()
            is_onK = False

        else:
            key_button.config(image = on)
            textLabel.config(text = "Keyboard is locked", fg = "green")
            Funcs.key_lock()
            is_onK = True

    def mouse_switch(event):
        global is_onM

        if is_onM:
            mouse_button.config(image = off)
            text2Label.config(text = "Mouse is unlocked", fg = "grey")
            Funcs.mouse_unlock()
            is_onM = False

        else:
            mouse_button.config(image = on)
            text2Label.config(text = "Mouse is locked\nPress Enter to unlock", fg = "green")
            Funcs.mouse_lock()
            is_onM = True
            if is_onK == True and is_onM == True: #activates keyboard if deactivated
                key_switch()

    on = tk.PhotoImage(file = "images/res-switch-on.png")
    off = tk.PhotoImage(file = "images/res-switch-off.png")

    key_button = tk.Button(root, image = off, bd = 0, command = key_switch)
    key_button.grid(column = 1, row = 0, sticky = 'ne')

    mouse_button = tk.Button(root, image = off, bd = 0)
    mouse_button.bind('<Button>', mouse_switch)
    root.bind('<Return>', mouse_switch)
    mouse_button.grid(column = 1, row = 2, sticky = 'ne')

    root.mainloop()

if __name__ == '__main__':
    is_onK = False
    is_onM = False
    main()