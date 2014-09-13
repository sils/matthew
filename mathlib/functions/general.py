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


def _exit(x=0, glob_vars={}):
    sys.exit(x)


def _print(*args, glob_vars={}):
    for arg in args:
        if arg[0] == arg[-1] == '"':
            print(arg[1:-1], end="")
            continue

        if str(arg).lower() in glob_vars:
            print(glob_vars[str(arg).lower()], end="")
            continue

        print(arg, end="")

    print()


def _return(*args, glob_vars={}):
    s, ok = generate_function(*args, glob_vars=glob_vars)
    return eval(s)


def makevar(variable, glob_vars={}):
    if variable.strip() == "":
        return " ", True
    if variable in glob_vars:
        return "glob_vars[\""+variable+"\"]", True

    if variable.replace(".", "", 1).isnumeric():
        return variable, True

    return "glob_vars[\""+variable+"\"]", False


variable_chars = string.ascii_letters + "_" + string.digits
operator_chars = "+-*/%(),"
def generate_function(*args, glob_vars={}):
    save_str = ""
    unknown_vars = []
    for arg in args:
        variable = ""
        for char in arg:
            if char in operator_chars:
                s, allok = makevar(variable, glob_vars)
                if not allok:
                    unknown_vars.append(variable)
                save_str += s + char
                variable = ""
            else:
                variable += char

        s, allok = makevar(variable, glob_vars)
        if not allok:
            unknown_vars.append(variable)
        save_str += s
    return save_str, unknown_vars


def save_eval(*args, glob_vars={}):
    val, unknown = generate_function(*args, glob_vars=glob_vars)
    if len(unknown) > 0:
        print("The following variables are undefined:")
        for var in unknown:
            print("  {}".format(var))
        print("Evaluation not possible.")
        return None

    return eval(val)


def let(var, be, *vals, glob_vars={}):
    if len(vals) < 1 or be.lower() != "be":
        print("Invalid syntax: use 'let <yourvar> be <yourval(s)>'")

    val = save_eval(*vals, glob_vars=glob_vars)
    if val is None:
        return False

    glob_vars[var] = val
    return val
