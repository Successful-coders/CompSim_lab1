import matplotlib.pyplot as plot


def drawHistogram(ys, spans):
    plot.hist(ys, spans)
    plot.show()
