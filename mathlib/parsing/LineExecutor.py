import inspect
import sys

__author__ = 'lasse'


class LineExecutor:
    ANS = "ans"

    def __init__(self, commands={}, glob_vars={}):
        """
        :param commands: dictionary with command (string) as index and function pointer as value
        :param vars: dictionary with variable name (string) as index and variable as value
        """
        self.commands = commands
        self.glob_vars = glob_vars

    def exec_line(self, line):
        components = str(line).strip().lower().split(" ")
        if len(components) < 1:
            return None

        command = components[0]
        args = components[1:]

        if not command in self.commands:
            print("This command '{}' is unsupported.".format(command))
            return None

        # Check nargs
        cmd = self.commands[command]
        argspec = inspect.getfullargspec(cmd)
        minlen = len(argspec.args if argspec.args != None else [])\
                 - len(argspec.defaults if argspec.defaults != None else [])
        if len(args) < minlen:
            print("The command '{}' needs at least {} argument(s). ({} given.)".format(command, minlen, len(args)))
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

def atest(arg1, a2=3, *args, defarg=2, **kwargs):
    pass
