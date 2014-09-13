from matplotlib import pyplot
from mathlib.functions.general import generate_function

__author__ = 'lasse'

def plot(*args, glob_vars={}):
    func_str, unknowns = generate_function(*args, glob_vars=glob_vars)

    ylabel = ''
    for arg in args:
        ylabel += " "+arg
    pyplot.ylabel(ylabel)

    if len(unknowns) == 0:
        x = [-10,10]
        y = eval(func_str)
        pyplot.plot(x, [y, y])
        pyplot.grid(True)
        pyplot.show()
        return True

    if len(unknowns) == 1:
        glob_vars[unknowns[0]] = 0
        y = []
        x = []
        for x_scaled in range(-100, 100, 1):
            glob_vars[unknowns[0]] = x_scaled/10
            x.append(glob_vars[unknowns[0]])
            y.append(eval(func_str))

        pyplot.plot(x, y)
        pyplot.xlabel(unknowns[0])
        pyplot.grid(True)

        pyplot.show()

        del glob_vars[unknowns[0]]
        return True

    print("Too many unknown variables. Only up to one dimensional functions can be plotted.")
    print(unknowns)
    return False
