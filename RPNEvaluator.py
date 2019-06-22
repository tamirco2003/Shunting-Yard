import math
from inspect import signature
from Operations import functions, operators

# Evaluates RPN to produce output.
def evalRPN(expression):
	stack = [] # Output stack.

	# For each token...
	for token in expression:
		# If number, add to stack.
		if type(token) == int or type(token) == float:
			stack.append(token)
		
		# If string...
		elif type(token) == str:
			# If function, pop needed params from stack and add function result back.
			if token in functions.keys():
				params = len(signature(functions[token]).parameters)
				operands = [stack.pop() for _ in range(params)]
				operands.reverse()
				stack.append(functions[token](*operands))

			# If operator, pop 2 operands from stack and add result back.
			elif token in operators.keys():
				operand2 = stack.pop()
				operand1 = stack.pop()
				stack.append(operators[token].function(operand1, operand2))

			# If "(", a pair of parentheses wasn't closed.
			elif token == "(":
				raise Exception("Missing \")\"")
			
			# Otherwise, raise an exception for unknown value.
			else:
				raise Exception("\"" + token + "\" isn't a possible value.")
	
	# Return stack.
	return stack
