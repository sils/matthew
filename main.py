from math import sin, exp
from mathlib.functions.all import commands
from mathlib.parsing.LineExecutor import LineExecutor

__author__ = 'lasse'

if __name__ == '__main__':
    le = LineExecutor(commands=commands,
                      glob_vars={
                          "ans": None,
                          "sin": sin,
                          "exp": exp
                      })

    prompt = "> "
    while True:
        le.exec_line(input(prompt))
