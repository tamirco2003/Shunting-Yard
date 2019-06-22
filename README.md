# Shunting Yard and RPN Evaluator
Literally an implementation of the [shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) written at 6 AM.

I was curious about parsing *M A T H* and found out about this algorithm. Pretty cool and interesting.

This also includes a [reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) evaluator, since shunting yard produces an RPN expression.

RPN is easy for computers to interpret since it does not have an order of operations, but is just evaluated left to right.

## How to use
`main.py` shows how you can use these to evaluate expressions writted in algebraic notation using the built in "calculate" function, which is itself in the same file.