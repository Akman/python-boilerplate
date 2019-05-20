""" sample/cli.py """

import curses
import sample.utils.hello


def main():
    """Entry point for the console script"""
    screen = curses.initscr()
    screen.clear()
    print(sample.utils.hello.get_greeting())
    return 0
