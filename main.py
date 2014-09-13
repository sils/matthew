import math
from mathlib.functions.all import commands
from mathlib.parsing.LineExecutor import LineExecutor

__author__ = 'lasse'

if __name__ == '__main__':
    le = LineExecutor(commands=commands,
                      glob_vars={
                          "ans": None,
                          "sin": math.sin,
                          "cos": math.cos,
                          "sinh": math.sinh,
                          "cosh": math.cosh,
                          "asin": math.asin,
                          "acos": math.acos,
                          "asinh": math.asinh,
                          "acosh": math.acosh,
                          "exp": math.exp,
                          "e": math.e,
                          "pi": math.pi,
                          "pow": pow
                      })

    prompt = "> "
    while True:
        le.exec_line(input(prompt))
