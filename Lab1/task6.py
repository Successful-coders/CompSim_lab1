import numpy as np
import matplotlib.pyplot as plot


def drawGraph(xs, ys):
    plot.plot(xs, ys)
    plot.xlabel('x')
    plot.ylabel('y')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.axvline(x=0, color='k')
    plot.show()
