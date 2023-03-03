import subprocess
import shutil

def is_valid_command(command):
    try:
        # Use `shutil.which` to check if the given command is in PATH
        path = shutil.which(command)
        if path is None:
            raise Exception("Not valid command")
        return True
    except Exception as e:
        print(e)
        return False

while True:
    command = input("Enter a command (Q to quit): ")
    if command == "Q":
        break
    if is_valid_command(command):
        try:
            subprocess.run([command], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {e}")
