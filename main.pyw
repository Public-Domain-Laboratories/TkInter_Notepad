def main():
    # Resolve text bluryness on Windows Operating System.
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

    # Import TkInterface and show the version.

    import tkinter
    print("TkVersion:", tkinter.TkVersion)

    # The Main Program.

    from tkinter import Tk, ttk, messagebox, font  

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

    frame = ttk.Frame(mainwindow, padding=0)
    frame.grid(sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))

    # Configure mainwindow grid
    mainwindow.columnconfigure(0, weight=1)
    mainwindow.rowconfigure(0, weight=1)

    # Text widget
    font = font.Font(family="Segoe UI", size=11, weight="normal")
    editortextwidget = tkinter.Text(frame, wrap='none', font=font, insertwidth=1, insertofftime=300, insertontime=600)
    editortextwidget.grid(row=1, column=0, columnspan=2, sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W), padx=0, pady=0)

    # Create vertical scrollbar and link it to the text widget
    verticalscrollbar = ttk.Scrollbar(frame, command=editortextwidget.yview)
    verticalscrollbar.grid(row=1, column=2, sticky=(tkinter.N, tkinter.S))
    editortextwidget.config(yscrollcommand=verticalscrollbar.set)

    # Create horizontal scrollbar and link it to the text widget
    horizontalscrollbar = ttk.Scrollbar(frame, orient="horizontal", command=editortextwidget.xview)
    horizontalscrollbar.grid(row=2, column=0, columnspan=2, sticky=(tkinter.E, tkinter.W))
    editortextwidget.config(xscrollcommand=horizontalscrollbar.set)

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)


  # Bind double-click event to the text widget
    def select_line_to_end(event):
        editortextwidget.tag_remove("sel", "1.0", "end")
        cursor_position = editortextwidget.index(tkinter.INSERT)
        line_start = f"{cursor_position} linestart"
        line_end = f"{cursor_position} lineend"
        editortextwidget.tag_add("sel", line_start, line_end)
        return "break"

    editortextwidget.bind("<Double-1>", select_line_to_end)


    # MenuBar

    def about(event):
        messagebox.showinfo("About", "Notepad running on TkInter " +  str(tkinter.TkVersion) + "\nPublic Domain Laboratories")

    menubar = tkinter.Menu(mainwindow)
    menufile = tkinter.Menu(menubar, tearoff=0)
    menufile.add_command(
        label="New", command=None, accelerator="Ctrl+N")
    menufile.add_command(
        label="New Window", command=None, accelerator="Ctrl+Shift+N")
    menufile.add_command(
        label="Open", command=None, accelerator="Ctrl+O")
    menufile.add_command(
        label="Save", command=None, accelerator="Ctrl+S")
    menufile.add_command(
        label="Save As", command=None, accelerator="Ctrl+Shift+S")
    menufile.add_separator()
    menufile.add_command(
        label="Page Setup", command=None)
    menufile.add_command(
        label="Print", command=None, accelerator="Ctrl+P")
    menufile.add_separator()
    menufile.add_command(
        label="Exit", command=mainwindow.quit)
    menubar.add_cascade(
        label="File", menu=menufile)

    menuhelp = tkinter.Menu(menubar, tearoff=0)
    menuhelp.add_command(
        label="View Help", command=None)
    menuhelp.add_command(
        label="Send Feedback", command=None)
    menuhelp.add_separator()
    menuhelp.add_command(label="About Notepad", command=lambda: about(None), accelerator="Ctrl+i") #FIX: about() triggers function to execute immediately, need to pass Null
    menubar.bind_all('<Control-i>', about)
    menubar.add_cascade(
        label="Help", menu=menuhelp, accelerator="Ctrl+H")
    
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