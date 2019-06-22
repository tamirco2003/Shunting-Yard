import re

pattern = r"(?:\d+(?:\.\d+)?)|\+|\-|\*|\/|\^|\(|\)|[a-z]+"

def to_float(s):
    try:
        return float(s)
    except ValueError:
        return s

# Splits expression into strings and floats.
def Tokenizer(expression):
	expression = expression.lower().replace(" ", "")
	matches = re.findall(pattern, expression)
	return [to_float(match) for match in matches]
