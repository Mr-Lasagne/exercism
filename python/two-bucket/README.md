# Two Bucket: Instructions

- [Exception messages](#exception-messages)

Given two buckets of different size and which bucket to fill first, determine
how many actions are required to measure an exact number of litres by
strategically transferring fluid between the buckets.

There are some rules that your solution must follow:

- You can only do one action at a time.
- There are only 3 possible actions:
  1. Pouring one bucket into the other bucket until either:
     - the first bucket is empty
     - the second bucket is full
  2. Emptying a bucket and doing nothing to the other.
  3. Filling a bucket and doing nothing to the other.
- After an action, you may not arrive at a state where the starting bucket is
  empty and the other bucket is full.

Your program will take as input:

- the size of bucket one
- the size of bucket two
- the desired number of litres to reach
- which bucket to fill first, either bucket one or bucket two

Your program should determine:

- the total number of actions it should take to reach the desired number of
  litres, including the first fill of the starting bucket
- which bucket should end up with the desired number of litres - either bucket
  one or bucket two
- how many litres are left in the other bucket

Note: any time a change is made to either or both buckets counts as one (1)
action.

Example: Bucket one can hold up to 7 litres, and bucket two can hold up to 11
litres. Let's say at a given step, bucket one is holding 7 litres and bucket two
is holding 8 litres (7,8). If you empty bucket one and make no change to bucket
two, leaving you with 0 litres and 8 litres respectively (0,8), that counts as
one action. Instead, if you had poured from bucket one into bucket two until
bucket two was full, resulting in 4 litres in bucket one and 11 litres in bucket
two (4,11), that would also only count as one action.

Another Example: Bucket one can hold 3 litres, and bucket two can hold up to 5
litres. You are told you must start with bucket one. So your first action is to
fill bucket one. You choose to empty bucket one for your second action. For your
third action, you may not fill bucket two, because this violates the third rule
-- you may not end up in a state after any action where the starting bucket is
empty and the other bucket is full.

Written with <3 at [Fullstack Academy][fullstack] by Lindsay Levine.

## Exception messages

Sometimes it is necessary to [raise an exception][raising-exceptions]. When you
do this, you should always include a **meaningful error message** to indicate
what the source of the error is. This makes your code more readable and helps
significantly with debugging. For situations where you know that the error
source will be a certain type, you can choose to raise one of the [built in
error types][base-classes], but should still include a meaningful message.

This particular exercise requires that you use the [raise
statement][the-raise-statement] to "throw" a `ValueError`. The tests will only
pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the
`exception` type:

```python
raise ValueError("A meaningful error message here.")
```

[base-classes]: https://docs.python.org/3/library/exceptions.html#base-classes
[fullstack]: https://www.fullstackacademy.com/
[raising-exceptions]:
  https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[the-raise-statement]:
  https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
