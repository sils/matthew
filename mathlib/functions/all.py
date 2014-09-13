__author__ = 'lasse'

from mathlib.functions import general, plotting

commands = {
    "exit": general._exit,
    "print": general._print,
    "return": general._return,
    "let": general.let,
    "eval": general.save_eval,
    "plot": plotting.plot
}

import math

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
}
