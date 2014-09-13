from mathlib.functions.all import commands, glob_vars
from mathlib.parsing.LineExecutor import LineExecutor

__author__ = 'lasse'

if __name__ == '__main__':
    le = LineExecutor(commands=commands,
                      glob_vars=glob_vars)

    prompt = "> "
    while True:
        le.exec_line(input(prompt))
