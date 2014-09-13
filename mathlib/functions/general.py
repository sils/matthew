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
