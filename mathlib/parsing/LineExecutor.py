import inspect
import sys

__author__ = 'lasse'


class LineExecutor:
    ANS = "ans"

    def __init__(self, commands={}, glob_vars={"ans": None}):
        """
        :param commands: dictionary with command (string) as index and function pointer as value
        :param vars: dictionary with variable name (string) as index and variable as value
        """
        self.commands = commands
        self.glob_vars = glob_vars

    def exec_line(self, line):
        command, args = self.parse_line(line)
        if command is None: return

        if not command in self.commands:
            print("This command '{}' is unsupported.".format(command))
            return None

        cmd = self.commands[command]
        if not self.check_command(cmd, command, len(args)):
            return

        # Execute!
        try:
            retval = cmd(*args, glob_vars=self.glob_vars)
            self.glob_vars[self.ANS] = retval
        except:
            print("An unknown error occurred.")
            return

        print("Command '{}' returned: {} = {}".format(command, self.ANS, retval))

        return retval

    def parse_line(self, line):
        # FIXME: obey ""s
        components = str(line).strip().lower().split(" ")
        if len(components) < 1:
            return None, None

        return components[0], components[1:]

    def check_command(self, cmd, cmdname, numargs):
        # Check nargs
        argspec = inspect.getfullargspec(cmd)
        minlen = len(argspec.args if argspec.args != None else [])\
                 -len(argspec.defaults if argspec.defaults != None else [])

        if numargs < minlen:
            print("Not enought arguments. The command '{}' needs at least {} argument(s). ({} given.)".format(cmdname,
                                                                                                              minlen,
                                                                                                              numargs))
            return False

        if argspec.varargs is None:
            maxlen = len(argspec.args if argspec.args != None else [])
            if "glob_vars" in argspec.args:
                maxlen -= 1
            if numargs > maxlen:
                print("Too many arguments. The command '{}' supports {} to {} argument(s). ({} given.)".format(cmdname,
                                                                                                               minlen,
                                                                                                               maxlen,
                                                                                                               numargs))
                return False

        return True

def atest(arg1, a2=3, *args, defarg=2, **kwargs):
    pass
