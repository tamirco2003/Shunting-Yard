from Operations import functions, operators

# Turns token list to RPN format.
def ShuntingYard(expression):
    output = [] # Output list.
    stack = [] # Operator stack.

	# For each token...
    for token in expression:
		# If number, add to output.
        if type(token) == int or type(token) == float:
            output.append(token)
		
		# If function, add to operator stack.
        elif token in functions.keys():
            stack.append(token)

		# If operator...
        elif token in operators:
			# While the operator should go after the top of the operators stack, pop to output.
            while len(stack) > 0 and (stack[-1] in functions.keys()
                                      or (stack[-1] in operators
                                          and (operators[stack[-1]].precedence > operators[token].precedence
                                               or (operators[stack[-1]].precedence == operators[token].precedence
                                                   and operators[stack[-1]].associativity == 0
                                                   )
                                               )
                                          )
                                      ) and stack[-1] != "(":
                output.append(stack.pop())
			# Add to operator stack.
            stack.append(token)

		# If "(", add to operator stack.
        elif token == "(":
            stack.append(token)

		# If ")", pop from operator stack to output until "(" is at the top of the stack.
        elif token == ")":
            try:
                while stack[-1] != "(":
                    output.append(stack.pop())
            except:
                raise Exception("Missing \"(\"")
            stack.pop()

		# Otherwise, raise an exception for unknown value.
        else:
            raise Exception("\"" + token + "\" isn't a possible value.")
	
	# If there is anything left at the operator stack, pop to output.
    while len(stack) > 0:
        output.append(stack.pop())

	# Return output.
    return output
