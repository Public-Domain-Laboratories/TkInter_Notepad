import sys
import os
import subprocess

def is_running_with_pythonw():
    executable_path = sys.executable
    executable_name = os.path.basename(executable_path)
    return executable_name.lower() == 'pythonw.exe'

def rerun_with_python():
    executable_path = sys.executable
    script_path = os.path.abspath(sys.argv[0])
    args = sys.argv[1:]
    
    python_executable = executable_path.replace('pythonw.exe', 'python.exe')
    
    # Rebuild the command with the python executable and original arguments
    command = [python_executable, script_path] + args

    # Run the command in the same command prompt
    os.execv(python_executable, command)

if __name__ == "__main__":
    if is_running_with_pythonw():
        print("Rerunning script with python.exe")
        rerun_with_python()
    else:
        print("The script is running with python.")
        # Your main script logic here
        input("Press Enter to continue...")
