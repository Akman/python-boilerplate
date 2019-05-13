""" Module curses """

import sys
import curses

def run():
    screen = curses.initscr()
    screen.clear()
    print(sys.path)
    print("Привет!")
    print("Python!")
