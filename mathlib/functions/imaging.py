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
from math import exp

import matplotlib.image as mpimage
from mathlib.output.ConsolePrinter import ConsolePrinter
from mathlib.functions.general import save_eval
from numpy import *


def load(img, into, varname, glob_vars={}, printer=ConsolePrinter()):
    if into.lower() != "into":
        printer.print("Invalid syntax: use 'load <path> into <yourvar>'", color="red")

    # FIXME check path
    glob_vars[varname.lower().strip()] = mpimage.imread(img)


'''def convolute(*args, glob_vars={}, printer=ConsolePrinter()):
    if not "and" in args:
        printer.print("Invalid syntax: use 'convolute <expr> and <expr>'", color="red")

    curr = 0
    first = ""
    second = ""
    for arg in args:
        if arg != "and":
            if curr == 0:
                first += arg
            else:
                second += arg

        curr += 1

    first = save_eval(first, glob_vars=glob_vars, printer=printer)
    second = save_eval(second, glob_vars=glob_vars, printer=printer)

    if first is None or second is None:
        return False'''

def point_spread_function(x, y=0, sigma=1):
    return exp(-(x*x + y*y)/(sigma*sigma))

def convolute_with_psf(*args, glob_vars={}, printer=ConsolePrinter()):
    var = save_eval(*args, glob_vars=glob_vars, printer=printer)
    if "sigma" in glob_vars:
        printer.print("Variable sigma is defined. Taking it to scale point spread function...")
        sigma = glob_vars["sigma"]
    else:
        printer.print("Variable sigma is undefined. Taking 1...")
        sigma = 1

    if not isinstance(var, ndarray):
        printer.print("Convolution is only possible with matrices/vectors right now.", color="red")

    dim = len(var.shape)
    assert dim == 3

    result = zeros(var.shape)
