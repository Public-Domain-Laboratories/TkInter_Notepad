
def main():
    # Resolve text bluryness on Windows Operating System.
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

    # Import TkInterface and show the version.

    import tkinter
    print("TkVersion:", tkinter.TkVersion)

    # The Main Program.

    from tkinter import Tk, ttk, messagebox  

    mainwindow = Tk()
    mainwindow.title("Untitled - Notepad")
    mainwindow.geometry("800x400")
    mainwindow.update()
    on_window_open(mainwindow)

    # Debug information
    print(str(mainwindow.winfo_geometry()))

    # Handle Program Window Exit.

    def on_closing():
        with open('notepad_user_settings_last_mainwindow_geometry.txt', 'w') as file: 
            file.write(str(mainwindow.winfo_geometry()))
        print("closing")

    def on_exit():
        on_closing()
        mainwindow.destroy()

    mainwindow.protocol("WM_DELETE_WINDOW", on_exit)

    # User Interface

    frame = ttk.Frame(mainwindow, padding=10)
    frame.grid()
    ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=on_exit).grid(column=1, row=0)

    def donothing():
        pass

    def about():
        messagebox.showinfo("About", "Notepad running on TkInter " +  str(tkinter.TkVersion) + "\nPublic Domain Laboratories")

    menubar = tkinter.Menu(mainwindow)
    menufile = tkinter.Menu(menubar, tearoff=0)
    menufile.add_command(label="New", command=donothing, accelerator="Ctrl+N")
    menufile.add_command(label="New Window", command=donothing, accelerator="Ctrl+Shift+N")
    menufile.add_command(label="Open", command=donothing, accelerator="Ctrl+O")
    menufile.add_command(label="Save", command=donothing, accelerator="Ctrl+S")
    menufile.add_command(label="Save As", command=donothing, accelerator="Ctrl+Shift+S")
    menufile.add_separator()
    menufile.add_command(label="Page Setup", command=donothing)
    menufile.add_command(label="Print", command=donothing, accelerator="Ctrl+P")
    menufile.add_separator()
    menufile.add_command(label="Exit", command=mainwindow.quit)
    menubar.add_cascade(label="File", menu=menufile)

    menuhelp = tkinter.Menu(menubar, tearoff=0)
    menuhelp.add_command(label="View Help", command=donothing)
    menuhelp.add_command(label="Send Feedback", command=donothing)
    menuhelp.add_separator()
    menuhelp.add_command(label="About Notepad", command=about, accelerator="Ctrl+i")
    menubar.add_cascade(label="Help", menu=menuhelp, accelerator="Ctrl+H")
    
    mainwindow.config(menu=menubar)

    # Start of the Program
    mainwindow.mainloop()

def on_window_open(mainwindow):
    import os
    if os.path.exists('notepad_user_settings_last_mainwindow_geometry.txt'):
        mainwindow.geometry(open('notepad_user_settings_last_mainwindow_geometry.txt').read())
        mainwindow.update()
        print("Window has been opened!")
        
if __name__=="__main__":

    import argparse

    # Create the parser
    parser = argparse.ArgumentParser(description='A Notepad program.')

    # Add the arguments
    parser.add_argument('-filename', type=str, help='the name of the file')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')

    # Parse the arguments
    args = parser.parse_args()
   
    # Use the arguments
    print(f'Filename: {args.filename}')
    if args.verbose:
        print('Verbosity turned on')
    else:
        print('Verbosity turned off')

    # If Notepad is installed on the system, look up previous settings.
    # system-wide user settings path: c:\Program Files\application-name

    main()