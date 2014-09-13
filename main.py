from mathlib.parsing.LineExecutor import LineExecutor

__author__ = 'lasse'


def _print(*args, glob_vars={}):
    print(*args)

def _exit(glob_vars={}):
    exit(0)

if __name__ == '__main__':
    le = LineExecutor(commands={
        "print": _print,
        "exit": _exit
    })

    prompt = "> "
    while True:
        le.exec_line(input(prompt))
