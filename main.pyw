
def main():
    # Resolve text bluryness on Windows Operating System.
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

    # Import TkInterface and show the version.

    import tkinter
    print("TkVersion:", tkinter.TkVersion)

    # The Main Program.

    from tkinter import Tk, ttk  

    window = Tk()
    window.title("Notepad")
    window.geometry("800x400")
    window.update()
    on_window_open(window)

    # Debug information
    print(str(window.winfo_geometry()))


    # Handle Program Window Exit.

    def on_closing():
        with open('notepad_user_settings_last_window_geometry.txt', 'w') as file: 
            file.write(str(window.winfo_geometry()))
        print("closing")

    def on_exit():
        on_closing()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_exit)





    # User Interface

    frame = ttk.Frame(window, padding=10)
    frame.grid()
    ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=on_exit).grid(column=1, row=0)

    window.mainloop()

def on_window_open(window):
    import os
    if os.path.exists('notepad_user_settings_last_window_geometry.txt'):
        window.geometry(open('notepad_user_settings_last_window_geometry.txt').read())
        print("Window has been opened!")
        
if __name__=="__main__":

    # Handle Command Line Interface
        # main --install 
        # Installs the program to store per-user or system-wide settings.
    import argparse

    # Create the parser
    parser = argparse.ArgumentParser(description='A Notepad program.')

    # Add the arguments
    parser.add_argument('filename', type=str, help='the name of the file')
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