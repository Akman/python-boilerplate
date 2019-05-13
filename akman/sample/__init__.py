from .hello import run as hello_run
from .show import run as show_run
from .curses import run as curses_run

"""Entry point for the main application script"""
def main():
    try:
        hello_run()
        show_run()
        curses_run()
        return 0
    except:
        return 1

if __name__ == "__main__":
    exit (main())
