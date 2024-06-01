import tkinter
print("TkVersion:", tkinter.TkVersion)

from tkinter import Tk, ttk  

window = Tk()
window.title("Notepad")
window.maxsize(1000, 400)

frame = ttk.Frame(window, padding=10)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=window.destroy).grid(column=1, row=0)
window.mainloop()