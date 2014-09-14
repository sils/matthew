"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import traceback

from matplotlib import pyplot
from numpy import *
from mathlib.functions.general import generate_function
from mathlib.output.ConsolePrinter import ConsolePrinter
import sys


def plot(*args, glob_vars={}, printer=ConsolePrinter()):
    func_str, unknowns = generate_function(*args, glob_vars=glob_vars, printer=printer)

    ylabel = ''
    for arg in args:
        ylabel += " "+arg
    ylabel = ylabel.strip()
    pyplot.ylabel(ylabel)

    if len(unknowns) == 0:
        printer.print("Plotting '{}' with no variables...".format(ylabel))
        try:
            y = eval(func_str)

            if isinstance(y, ndarray):
                if len(y.shape) > 2:
                    pyplot.imshow(y)
                else:
                    pyplot.plot(y)
            else:
                x = [-10, 10]
                pyplot.plot(x, [y, y])

            pyplot.grid(True)
            pyplot.show()
            return True
        except:
            traceback.print_tb(sys.exc_info()[2])
            print(sys.exc_info())
            printer.print("Cannot evaluate expresssion. Aborting plot...",
                          color="red")
            return False

    if len(unknowns) == 1:
        unknown = unknowns[0]
        printer.print("Plotting '{}' with variable '{}'...".format(ylabel, unknown))
        glob_vars[unknown] = 0
        y = []
        x = []
        evaluation_failures = 0
        for x_scaled in range(-100, 100, 1):
            glob_vars[unknown] = x_scaled/10
            try:
                s = eval(func_str)
                x.append(glob_vars[unknown])
                y.append(s)
                evaluation_failures = 0
            except:
                printer.print("Failed evaluating function for {}={}. (Singularity?)".format(unknown, glob_vars[unknown]))
                evaluation_failures += 1
                if evaluation_failures > 10:
                    printer.print("There were 10 evaluation failures in a row. "
                                  "Assuming function is not plottable. Aborting plot...", color="red")
                    del glob_vars[unknown]
                    return False

        pyplot.plot(x, y)
        pyplot.xlabel(unknown)
        pyplot.grid(True)

        pyplot.show()

        del glob_vars[unknown]
        return True

    printer.print("Too many unknown variables. Only up to one dimensional functions can be plotted.", color="red")
    printer.print("Unknown variables are:", unknowns)
    return False
