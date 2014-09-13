import string

__author__ = 'lasse'


def _exit(x=0, glob_vars={}):
    exit(x)


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
    return save_eval(*args, glob_vars=glob_vars)


def get_value(var, glob_vars={}):
    var = str(var)
    if not var in glob_vars:
        return var

    return glob_vars[var]


variable_chars = string.ascii_letters + "_" + string.digits
operator_chars = "+-*/%"
allowed_chars = variable_chars + operator_chars
def save_eval(*args, glob_vars={}):
    save_str = ""
    for arg in args:
        variable = ""
        for char in arg:
            if char in allowed_chars:
                if char in operator_chars:
                    save_str += str(get_value(variable, glob_vars)) + char
                    variable = ""
                else:
                    variable += char

        save_str += str(get_value(variable, glob_vars))

    return eval(save_str)


def let(var, be, *vals, glob_vars={}):
    if len(vals) < 1 or be.lower() != "be":
        print("Invalid syntax: use 'let <yourvar> be <yourval(s)>'")

    glob_vars[var] = save_eval(*vals, glob_vars=glob_vars)
    return glob_vars[var]
