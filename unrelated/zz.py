import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def main():
    # Import TkInterface and show the version.
    import tkinter
    print("TkVersion:", tkinter.TkVersion)

    # The Main Program.
    from tkinter import Tk

    mainwindow = Tk()
    mainwindow.title("Simple Text Editor")
    mainwindow.geometry("800x600")
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
    text_widget = tk.Text(mainwindow, wrap='none', font="Segoe 10")
    text_widget.pack(fill=tk.BOTH, expand=True)

    vbar = ttk.Scrollbar(mainwindow, command=text_widget.yview)
    vbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget.config(yscrollcommand=vbar.set)

    hbar = ttk.Scrollbar(mainwindow, orient="horizontal", command=text_widget.xview)
    hbar.pack(side=tk.BOTTOM, fill=tk.X)
    text_widget.config(xscrollcommand=hbar.set)

    # MenuBar
    def new_file():
        text_widget.delete('1.0', tk.END)
        mainwindow.title("Simple Text Editor")
        global current_file
        current_file = None

    def open_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                text_widget.delete('1.0', tk.END)
                text_widget.insert('1.0', content)
            mainwindow.title(f"Simple Text Editor - {file_path}")
            global current_file
            current_file = file_path

    def save_file():
        global current_file
        if current_file:
            with open(current_file, 'w') as file:
                file.write(text_widget.get('1.0', tk.END))
        else:
            save_file_as()

    def save_file_as():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_widget.get('1.0', tk.END))
            mainwindow.title(f"Simple Text Editor - {file_path}")
            global current_file
            current_file = file_path

    def cut():
        copy()
        text_widget.delete("sel.first", "sel.last")

    def copy():
        mainwindow.clipboard_clear()
        mainwindow.clipboard_append(text_widget.selection_get())

    def paste():
        text_widget.insert(tk.INSERT, mainwindow.clipboard_get())

    def about(event=None):
        messagebox.showinfo("About", "Simple Text Editor running on TkInter " + str(tkinter.TkVersion))

    menubar = tk.Menu(mainwindow)
    menufile = tk.Menu(menubar, tearoff=0)
    menufile.add_command(label="New", command=new_file, accelerator="Ctrl+N")
    menufile.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
    menufile.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
    menufile.add_command(label="Save As", command=save_file_as, accelerator="Ctrl+Shift+S")
    menufile.add_separator()
    menufile.add_command(label="Exit", command=on_exit)
    menubar.add_cascade(label="File", menu=menufile)

    menuedit = tk.Menu(menubar, tearoff=0)
    menuedit.add_command(label="Cut", command=cut)
    menuedit.add_command(label="Copy", command=copy)
    menuedit.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=menuedit)

    menuhelp = tk.Menu(menubar, tearoff=0)
    menuhelp.add_command(label="About Simple Text Editor", command=lambda: about(None), accelerator="Ctrl+I")
    menubar.bind_all('<Control-i>', about)
    menubar.add_cascade(label="Help", menu=menuhelp)

    mainwindow.config(menu=menubar)

    # Start of the Program
    mainwindow.mainloop()

def on_window_open(mainwindow):
    import os
    if os.path.exists('notepad_user_settings_last_mainwindow_geometry.txt'):
        mainwindow.geometry(open('notepad_user_settings_last_mainwindow_geometry.txt').read())
        mainwindow.update()
        print("Window has been opened!")

if __name__ == "__main__":
    import argparse

    # Create the parser
    parser = argparse.ArgumentParser(description='A Simple Text Editor program.')

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
    # system-wide user settings path: c:\\Program Files\\application-name

    main()
