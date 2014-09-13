from matplotlib import pyplot
from mathlib.functions.general import generate_function

__author__ = 'lasse'

def plot(*args, glob_vars={}):
    func_str, unknowns = generate_function(*args, glob_vars=glob_vars)

    ylabel = ''
    for arg in args:
        ylabel += " "+arg
    ylabel = ylabel.strip()
    pyplot.ylabel(ylabel)

    if len(unknowns) == 0:
        print("Plotting '{}' with no variables...".format(ylabel))
        x = [-10,10]
        y = eval(func_str)
        pyplot.plot(x, [y, y])
        pyplot.grid(True)
        pyplot.show()
        return True

    if len(unknowns) == 1:
        unknown = unknowns[0]
        print("Plotting '{}' with variable '{}'...".format(ylabel, unknown))
        glob_vars[unknown] = 0
        y = []
        x = []
        for x_scaled in range(-100, 100, 1):
            glob_vars[unknown] = x_scaled/10
            x.append(glob_vars[unknown])
            y.append(eval(func_str))

        pyplot.plot(x, y)
        pyplot.xlabel(unknown)
        pyplot.grid(True)

        pyplot.show()

        del glob_vars[unknown]
        return True

    print("Too many unknown variables. Only up to one dimensional functions can be plotted.")
    print("Unknown variables are:", unknowns)
    return False
