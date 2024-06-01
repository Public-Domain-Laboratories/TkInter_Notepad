


import tkinter
print("TkVersion:", tkinter.TkVersion)

from tkinter import Tk, ttk  

window = Tk()
window.title("Notepad")
window.geometry("800x400")
window.update()
print(str(window.winfo_reqwidth()) + "x" + str(window.winfo_reqheight()))
print(str(window.winfo_width ()) + "x" + str(window.winfo_height ()))

def on_closing():
    with open('notepad_user_settings_last_window_geometry.txt', 'w') as file: 
        window.update()
        file.write(str(window.winfo_width ()) + "x" + str(window.winfo_height ()) )
        print("closing")
        print(str(window.winfo_reqwidth()) + "x" + str(window.winfo_reqheight()))
        print(str(window.winfo_width ()) + "x" + str(window.winfo_height ()))
    # notepad_user_settings_last_window_position

def on_exit():
    on_closing()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_exit)

def on_window_open(window):
    import os
    if os.path.exists('notepad_user_settings_last_window_geometry.txt'):
        window.geometry(open('notepad_user_settings_last_window_geometry.txt').read())
        window.update()
        print("Window has been opened!")
window.bind('<Map>', on_window_open(window))


import argparse

# If Notepad is installed on the system, look up previous settings.
# system-wide user settings path: c:\Program Files\application-name


frame = ttk.Frame(window, padding=10)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=on_exit).grid(column=1, row=0)
window.mainloop()


