import Tokenizer
import ShuntingYard
import RPNEvaluator

# Take string expression and output it's value.
def calculate(expression):
    tokens = Tokenizer.Tokenizer(expression)
    RPNExp = ShuntingYard.ShuntingYard(tokens)
    return RPNEvaluator.evalRPN(RPNExp)

# Simple order of operations calculation.
print(calculate("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"))
# Result: [3.0001220703125]

# Calculate sine of 60 degrees.
print(calculate("sin(rad(60))"))
# Result: [0.8660254037844386]