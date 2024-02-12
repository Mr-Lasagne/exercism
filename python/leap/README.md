# Leap: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [Testing](#testing)

## Introduction

A leap year (in the Gregorian calendar) occurs:

- In every year that is evenly divisible by 4.
- Unless the year is evenly divisible by 100, in which case it's only a leap
  year if the year is also evenly divisible by 400.

Some examples:

- 1997 was not a leap year as it's not divisible by 4.
- 1900 was not a leap year as it's not divisible by 400.
- 2000 was a leap year!

For a delightful, four-minute explanation of the whole phenomenon of leap years,
check out [this YouTube video](https://www.youtube.com/watch?v=xX96xng7sAE).

This problem was based on [CodeRanch Cattle Drive, Assignment
3][coderanch-leap].

## Task

In a file called `leap.py`, implement a program that determines whether a given
year is a leap year. The program should include the following function:

- `is_leap_year` that takes an integer (_a year_) as an argument and returns a
  Boolean value (_True if the given year is a leap year, False otherwise_).

### Testing

In a file called `test_leap.py`, implement a test suite that covers the
following test cases:

```python
# Year not divisible by 4 is a common year.
>>> is_leap_year(2015)
False

# Year divisible by 2 and not by 4 is a common year.
>>> is_leap_year(1970)
False

# Year divisible by 4 and not by 100 is a leap year.
>>> is_leap_year(1996)
True

# Year divisible by 4 and 5 is still a leap year.
>>> is_leap_year(1960)
True

# Year divisible by 100 and not by 400 is a common year.
>>> is_leap_year(2100)
False

# Year divisible by 100 and not by 3 is a common year.
>>> is_leap_year(1900)
False

# Year divisible by 400 is a leap year.
>>> is_leap_year(2000)
True

# Year divisible by 400 and not by 125 is a leap year.
>>> is_leap_year(2400)
True

# Year divisible by 200 and not by 400 is a common year.
>>> is_leap_year(1800)
False
```

[coderanch-leap]: https://coderanch.com/t/718816/Leap
