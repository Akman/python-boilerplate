# -*- coding: utf-8 -*-

""" sample/gui.py """

import matplotlib.pyplot as plt
import numpy as np


def main():
    """ Entry point for gui """
    # Create a list of evenly-spaced numbers over the range
    point_x = np.linspace(0, 20, 100)
    # Plot the sine of each x point
    plt.plot(point_x, np.sin(point_x))
    # Display the plot
    plt.show()
