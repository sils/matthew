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

import matplotlib.image as mpimage
from mathlib.output.ConsolePrinter import ConsolePrinter


def load(img, into, varname, glob_vars={}, printer=ConsolePrinter()):
    if into.lower() != "into":
        printer.print("Invalid syntax: use 'load <path> into <yourvar>'", color="red")

    # FIXME check path
    glob_vars[varname] = mpimage.imread(img)

def convolute(*args, glob_vars={}, printer=ConsolePrinter()):
    if not "and" in args:
        printer.print("Invalid syntax: use 'convolute <expr> and <expr>'", color="red")
