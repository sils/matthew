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

import string
import sys
from numpy import *
from mathlib.output.NullPrinter import NullPrinter
from mathlib.output.ConsolePrinter import ConsolePrinter
from mathlib.parsing.LineExecutor import LineExecutor


def _exit(x=0, glob_vars={}, printer=ConsolePrinter()):
    sys.exit(x)


def _print(*args, glob_vars={}, printer=ConsolePrinter()):
    printer.print(*args)

    return glob_vars["ans"]


def makevar(variable, glob_vars={}, printer=ConsolePrinter()):
    variable = str(variable).lower().strip()
    if variable == "":
        return " ", True
    if variable in glob_vars:
        return "glob_vars[\""+variable+"\"]", True

    if variable.replace(".", "", 1).isnumeric():
        return variable, True

    return "glob_vars[\""+variable+"\"]", False


variable_chars = string.ascii_letters + "_" + string.digits
operator_chars = "+-*/%(),[]{}:"
def generate_function(*args, glob_vars={}, printer=ConsolePrinter()):
    save_str = ""
    unknown_vars = []
    open_square_brackets = 0
    for arg in args:
        variable = ""
        for char in arg:
            if char in operator_chars:
                s, allok = makevar(variable, glob_vars, printer=printer)
                if not allok and not variable in unknown_vars:
                    unknown_vars.append(variable)
                save_str += s
                variable = ""

                if char == "[":
                    open_square_brackets += 1
                    if open_square_brackets == 1:
                        save_str += "array(["
                    else: save_str += "["
                elif char == "]":
                    open_square_brackets -= 1
                    if open_square_brackets == 0:
                        save_str += "])"
                    else: save_str += "]"
                else:
                    save_str += char
            else:
                variable += char

        s, allok = makevar(variable, glob_vars, printer=printer)
        if not allok and not variable in unknown_vars:
            unknown_vars.append(variable)
        save_str += s

    return save_str, unknown_vars


def comment(*args, glob_vars={}, printer=ConsolePrinter()):
    return glob_vars["ans"]


def seperate_by_keywords(args, keywords):
    result = dict()
    curr = None
    i = 0
    for arg in args:
        if arg in keywords:
            if arg in result.keys():
                curr = arg+"__"+str(i)
                i += 1
            else:
                curr = arg
        else:
            if curr in result.keys():
                result[curr] += " "+arg
            else:
                result[curr] = arg
    return result

def _len(*args, glob_vars={}, printer=ConsolePrinter()):
    return len(save_eval(*args, glob_vars=glob_vars, printer=printer))

def save_eval(*args, glob_vars={}, printer=ConsolePrinter()):
    val, unknown = generate_function(*args, glob_vars=glob_vars, printer=printer)
    if len(unknown) > 0:
        printer.print("The following variables are undefined:")
        for var in unknown:
            printer.print("  {}".format(var))
        printer.print("Evaluation not possible.", color="red")
        return None

    return eval(val)


def help(glob_vars={}, printer=ConsolePrinter()):
    from mathlib.functions.all import commands
    printer.print("The following commands are available:")
    for key in commands.keys():
        printer.print("  {}".format(key))

    return True

def let(var, be, *vals, glob_vars={}, printer=ConsolePrinter()):
    if len(vals) < 1 or be.lower() != "be":
        printer.print("Invalid syntax: use 'let <yourvar> be <yourval(s)>'", color="red")

    val = save_eval(*vals, glob_vars=glob_vars, printer=printer)
    if val is None:
        return False

    glob_vars[var.lower().strip()] = val
    return val

def execute(f, glob_vars={}, printer=ConsolePrinter()):
    from mathlib.functions.all import commands
    # TODO take a logprinter here
    nullprinter = NullPrinter()
    parser = LineExecutor(commands=commands, glob_vars=glob_vars, printer=nullprinter)
    file = open(f, "r")
    lines = file.readlines()
    vars_before = glob_vars.copy().keys()
    for line in lines:
        printer.print(">> "+line.strip(" \n"))
        parser.exec_line(line)

    vars_after = glob_vars.keys()
    v = []
    for _var in vars_after:
        if not _var in vars_before:
            v.append(_var)

    printer.print("+-------------------------+")
    printer.print("|New variables introduced:|")
    printer.print("+-------------------------+")
    printer.print(str(v))

    return glob_vars["ans"]
