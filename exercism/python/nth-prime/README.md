# Nth Prime: Instructions

- [Exception messages](#exception-messages)

Given a number n, determine what the nth prime is.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

If your language provides methods in the standard library to deal with prime
numbers, pretend they don't exist and implement them yourself.

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
# when the prime function receives malformed input
raise ValueError('there is no zeroth prime')
```

[base-classes]: https://docs.python.org/3/library/exceptions.html#base-classes
[raising-exceptions]:
  https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[the-raise-statement]:
  https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
