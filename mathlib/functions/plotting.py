from math import sin
from matplotlib import pyplot

__author__ = 'lasse'

def plot(function, glob_vars={}):
    func = glob_vars[function]
    x=[]
    y = []
    for x_scaled in range(-100,100,1):
        unscaled = float(x_scaled/10)
        x.append(unscaled)
        y.append(float(func(unscaled)))

    pyplot.plot(x, y)
    pyplot.grid(True)
    pyplot.show()
