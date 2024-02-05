# Minesweeper: Instructions

- [Examples](#examples)
- [Exception messages](#exception-messages)

Add the mine counts to a completed Minesweeper board.

Minesweeper is a popular game where the user has to find the mines using numeric
hints that indicate how many mines are directly adjacent (horizontally,
vertically, diagonally) to a square.

In this exercise you have to create some code that counts the number of mines
adjacent to a given empty square and replaces that square with the count.

The board is a rectangle composed of blank space (' ') characters. A mine is
represented by an asterisk (`*`) character.

If a given space has no adjacent mines at all, leave that square blank.

## Examples

For example you may receive a 5 x 4 board like this (empty spaces are
represented here with the '·' character for display on screen):

```text
·*·*·
··*··
··*··
·····
```

And your code will transform it into this:

```text
1*3*1
13*31
·2*2·
·111·
```

## Exception messages

Sometimes it is necessary to [raise an exception][raising-exceptions]. When you
do this, you should always include a **meaningful error message** to indicate
what the source of the error is. This makes your code more readable and helps
significantly with debugging. For situations where you know that the error
source will be a certain type, you can choose to raise one of the [built in
error types][base-classes], but should still include a meaningful message.

This particular exercise requires that you use the [raise
statement][the-raise-statement] to "throw" a `ValueError` when the `board()`
function receives malformed input. The tests will only pass if you both `raise`
the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the
`exception` type:

```python
# when the board receives malformed input
raise ValueError("The board is invalid with current input.")
```

[base-classes]: https://docs.python.org/3/library/exceptions.html#base-classes
[raising-exceptions]:
  https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[the-raise-statement]:
  https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
