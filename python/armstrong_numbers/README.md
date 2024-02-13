# Armstrong Numbers: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [Testing](#testing)

## Introduction

An [Armstrong number][armstrong-number] is a number that is the sum of its own
digits each raised to the power of the number of digits.

For example:

- 9 is an Armstrong number, because `9 = 9^1 = 9`
- 10 is _not_ an Armstrong number, because `10 != 1^2 + 0^2 = 1`
- 153 is an Armstrong number, because:
  `153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`
- 154 is _not_ an Armstrong number, because:
  `154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190`

## Task

In a file called `armstrong_numbers.py`, implement a program that determines
whether a number is an Armstrong number. The program should include the
following function:

- `is_armstrong_number` that takes an integer (_a given positive integer_) as an
  argument and returns a Boolean value (_True if the number is an Armstrong
  number, False otherwise_).

### Testing

In a file called `test_armstrong_numbers.py`, implement a test suite that covers
the following test cases:

[armstrong-number]: https://en.wikipedia.org/wiki/Narcissistic_number
