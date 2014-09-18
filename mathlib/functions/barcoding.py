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
from numpy import *
from mathlib.functions.general import save_eval, seperate_by_keywords
from mathlib.output.ConsolePrinter import ConsolePrinter


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


def disturb(*args, glob_vars={}, printer=ConsolePrinter()):
    var = save_eval(*args, glob_vars=glob_vars, printer=printer)
    off = (random.random() - 0.5)*0.02
    res = []
    for val in var:
        res.append(val + (random.random()-0.5)*0.009 + off)

    return array(res)


def mmult(*args, glob_vars={}, printer=ConsolePrinter()):
    args = seperate_by_keywords(args, ["with"])
    first=save_eval(args[None], glob_vars=glob_vars, printer=printer)
    sec=save_eval(args["with"], glob_vars=glob_vars, printer=printer)
    return array(matrix(first)*matrix(sec))


def vmult(*args, glob_vars={}, printer=ConsolePrinter()):
    return mmult(*args, glob_vars=glob_vars, printer=printer)[0]


def point_spread_kernel(i, j, sigma, n):
    return 1/n * exp(-(i*i+j*j)/(sigma*sigma*n*n))


def index(_i, _j, n):
    return _i*n + _j
def ext_blur_matrix(n, m, sigma):
    result = zeros((n*m, n*m))
    for i in range(0, n):
        print("still iterating")
        for j in range(0, m):
            for _k in range(0, n):
                for l in range(0, m):
                    result[index(i, j, n)][index(_k, l, n)] = point_spread_kernel(i-_k, j-l, sigma, n*m)
    return result


def blur_matrix(n, sigma):
    a = zeros((n, n), dtype=float)

    for i in range(0, n):
        for j in range(0,n):
            a[i][j] = point_spread_kernel(i-j, 0, sigma, n)

    return array(a)
