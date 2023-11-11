# input.py
import sys
import shlex

def get_input():
    command = ""
    if len(sys.argv) > 1:
        command = shlex.join(sys.argv[1:])
        return command
    else:
        print("No command provided.")
        return None