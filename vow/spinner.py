# spinner.py
import itertools
import sys
import time

def spinner(stop_event):
    for cursor in itertools.cycle('|/-\\'):
        if stop_event.is_set():
            break
        sys.stdout.write(cursor)
        sys.stdout.flush()
        sys.stdout.write('\b')
        time.sleep(0.1)