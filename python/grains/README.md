# Grains: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [Exception messages](#exception-messages)
  - [Testing](#testing)

## Introduction

There once was a wise servant who saved the life of a prince. The king promised
to pay whatever the servant could dream up. Knowing that the king loved chess,
the servant told the king he would like to have grains of wheat. One grain on
the first square of a chess board, with the number of grains doubling on each
successive square.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has
two grains, and so on).

For more information see [CodeRanch Cattle Drive, Assignment
6][coderanch-grains] and [wheat and chessboard
problem][wheat-and-chessboard-problem].

## Task

In a file called `grains.py`, implement a program that calculates results
related to the wheat and chessboard problem. The program should include the
following functions:

- `square` that takes an integer (_the given square number_) as an argument and
  returns an integer (_the number of grains on the given square_).
- `total` that takes no arguments and returns an integer (_the total number of
  grains on the chessboard_).

### Exception messages

Sometimes it is necessary to [raise an exception][raising-exceptions]. When you
do this, you should always include a meaningful error message to indicate what
the source of the error is. This makes your code more readable and helps
significantly with debugging. For situations where you know that the error
source will be a certain type, you can choose to raise one of the [built in
error types][built-in-error-types], but should still include a meaningful
message.

This particular exercise requires that you use the [raise
statement][the-raise-statement] to "throw" a `ValueError` when the square input
is out of range. The tests will only pass if you both `raise` the `exception`
and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the
`exception` type:

```python
# When the square value is not in the acceptable range.
raise ValueError("Square must be between 1 and 64.")
```

### Testing

In a file called `test_grains.py`, implement a test suite that covers the
following test cases:

```python
# Grains on square 1.
>>> square(1)
1

# Grains on square 2.
>>> square(2)
2

# Grains on square 3.
>>> square(3)
4

# Grains on square 4.
>>> square(4)
8

# Grains on square 16.
>>> square(16)
32768

# Grains on square 32.
>>> square(32)
2147483648

# Grains on square 64.
>>> square(64)
9223372036854775808

# Square 0 is invalid.
>>> square(0)
ValueError("Square must be between 1 and 64.")

# Negative square is invalid.
>>> square(-1)
ValueError("Square must be between 1 and 64.")

# Square greater than 64 is invalid.
>>> square(65)
ValueError("Square must be between 1 and 64.")

# Total number of grains.
>>> total()
18446744073709551615
```

[built-in-error-types]:
  https://docs.python.org/3/library/exceptions.html#base-classes
[coderanch-grains]: https://coderanch.com/wiki/718824/Grains
[raising-exceptions]:
  https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[the-raise-statement]:
  https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
[wheat-and-chessboard-problem]:
  https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem
