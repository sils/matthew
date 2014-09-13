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

import inspect
import sys
from mathlib.output.ConsolePrinter import ConsolePrinter


class LineExecutor:
    ANS = "ans"

    def __init__(self, commands={}, glob_vars={"ans": None}, printer=ConsolePrinter()):
        """
        :param commands: dictionary with command (string) as index and function pointer as value
        :param vars: dictionary with variable name (string) as index and variable as value
        """
        self.commands = commands
        self.glob_vars = glob_vars
        self.printer = printer

    def exec_line(self, line):
        command, args = self.parse_line(line)

        if command == '':
            return

        if not command in self.commands:
            self.printer.print("The command '{}' is unsupported.".format(command))
            return None

        cmd = self.commands[command]
        if not self.check_command(cmd, command, len(args)):
            return

        # Execute!
        try:
            retval = cmd(*args, glob_vars=self.glob_vars, printer=self.printer)
            self.glob_vars[self.ANS] = retval
        except:
            e = sys.exc_info()
            if e[0] is SystemExit:
                raise e[1]

            self.printer.print("An error occurred. "
                               "It was an exception of the type '{}' with message '{}'.".format(e[0].__name__,
                                                                                                str(e[1])))
            return

        self.printer.print(" {} = {}".format(self.ANS, retval))

        return retval

    def parse_line(self, line):
        # FIXME: obey ""s
        components = str(line).strip().lower().split(" ")

        for key, val in enumerate(components):
            components[key] = val.strip()

        return components[0], components[1:]

    def check_command(self, cmd, cmdname, numargs):
        # Check nargs
        argspec = inspect.getfullargspec(cmd)
        minlen = len(argspec.args if argspec.args != None else [])\
                 -len(argspec.defaults if argspec.defaults != None else [])

        if numargs < minlen:
            self.printer.print("Not enought arguments. "
                               "The command '{}' needs at least {} argument(s). ({} given.)".format(cmdname,
                                                                                                    minlen,
                                                                                                    numargs))
            return False

        if argspec.varargs is None:
            maxlen = len(argspec.args if argspec.args != None else [])
            if "glob_vars" in argspec.args:
                maxlen -= 1
            if numargs > maxlen:
                self.printer.print("Too many arguments. "
                                   "The command '{}' supports {} to {} argument(s). ({} given.)".format(cmdname,
                                                                                                        minlen,
                                                                                                        maxlen,
                                                                                                        numargs))
                return False

        return True
