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


def _return(arg, glob_vars={}):
    return arg


def let(var, be, *vals, glob_vars={}):
    if len(vals) < 1 or be.lower() != "be":
        print("Invalid syntax: use 'let <yourvar> be <yourval(s)>'")

    if len(vals) == 1:
        vals = vals[0]

    glob_vars[var] = vals
    return vals
