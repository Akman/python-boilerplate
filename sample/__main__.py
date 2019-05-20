""" sample/__main__.py """

import sys
import sample.cli
import sample.gui

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        sample.gui.main()
    else:
        sample.cli.main()

if __name__ == "__main__":
    exit(main())
