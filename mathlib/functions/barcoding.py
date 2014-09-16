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
from numpy import *
from mathlib.functions.general import save_eval
from mathlib.output.ConsolePrinter import ConsolePrinter


def point_spread_kernel(i, j, sigma, n):
    return 1/n * exp(-pow((i-j)/(sigma*n), 2))


def convolute(*args, glob_vars={}, printer=ConsolePrinter()):
    var = save_eval(*args, glob_vars=glob_vars, printer=printer)
    if "sigma" in glob_vars:
        printer.print("Variable sigma is defined. Taking it to scale point spread function...")
        sigma = glob_vars["sigma"]
    else:
        printer.print("Variable sigma is undefined. Taking 1...")
        sigma = 1

    res = []
    for i in range(0, len(var)):
        this = 0
        for j in range(0, len(var)):
            this += point_spread_kernel(i, j, sigma, len(var)) * var[j]

        res.append(this)

    return array(res)


def mmult(*args, glob_vars={}, printer=ConsolePrinter()):
    pass


def blur_matrix(n, sigma):
    a = zeros((n,n), dtype=float)

    for i in range(0,n):
        for j in range(0,n):
            a[i][j] = point_spread_kernel(i,j,sigma,n)

    return array(a)
