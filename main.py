from tkinter import Tk, ttk

app = Tk()
app.title("Notepad")
app.maxsize(1000, 400)


frame = ttk.Frame(app, padding=10)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=app.destroy).grid(column=1, row=0)
app.mainloop()