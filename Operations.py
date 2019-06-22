import math


class operator:
    def __init__(self, precedence, associativity, function):
        self.precedence = precedence
        self.associativity = associativity
        self.function = function


operators = {
    "^": operator(2, 1, lambda a, b: a ** b),
    "/": operator(1, 0, lambda a, b: a / b),
    "*": operator(1, 0, lambda a, b: a * b),
    "-": operator(0, 0, lambda a, b: a - b),
    "+": operator(0, 0, lambda a, b: a + b),
}

functions = {
    "neg": lambda x: -x,
    "abs": lambda x: abs(x),
    "sqrt": lambda x: math.sqrt(x),
    "rad": lambda x: math.radians(x),
    "deg": lambda x: math.degrees(x),
    "sin": lambda x: math.sin(x),
    "cos": lambda x: math.cos(x),
    "tan": lambda x: math.tan(x),
	"asin": lambda x: math.asin(x),
	"acos": lambda x: math.acos(x),
	"atan": lambda x: math.atan(x),
	"max": lambda x, y: max(x, y),
	"min": lambda x, y: min(x, y),
	"log": lambda x, base: math.log(x, base),
	"ln": lambda x: math.log(x),
	"floor": lambda x: math.floor(x),
}
