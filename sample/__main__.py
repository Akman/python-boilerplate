""" sample/__main__.py """

import sys
import sample.cli
import sample.gui

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sample.gui.main()
    else:
        sample.cli.main()
    exit(0)
