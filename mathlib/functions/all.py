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

from mathlib.functions import general, plotting, imaging, barcoding

commands = {
    "exit": general._exit,
    "print": general._print,
    "return": general.save_eval,
    "let": general.let,
    "eval": general.save_eval,
    "plot": plotting.plot,
    "help": general.help,
    "load": imaging.load,
    "execute": general.execute,
    "blur": barcoding.convolute,
    "mmult": barcoding.mmult,
    "vmult": barcoding.vmult,
    "len": general._len,
    "invert": barcoding.invert,
    "disturb": barcoding.disturb,
    "#": general.comment,
    "//": general.comment
}

import math

glob_vars = {
    "ans": None,
    "sin": math.sin,
    "cos": math.cos,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "asin": math.asin,
    "acos": math.acos,
    "asinh": math.asinh,
    "acosh": math.acosh,
    "exp": math.exp,
    "e": math.e,
    "pi": math.pi,
    "pow": pow,
    "blur_matrix": barcoding.blur_matrix
}
