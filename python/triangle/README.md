# Triangle: Instructions

## Introduction

For a shape to be a triangle at all, all sides have to be of length > 0, and the
sum of the lengths of any two sides must be greater than or equal to the length
of the third side.

In equations:

Let `a`, `b`, and `c` be sides of the triangle. Then all three of the following
expressions must be true:

```text
a + b ≥ c
b + c ≥ a
a + c ≥ b
```

See [Triangle Inequality][triangle-inequality] and [The Ruby Koans triangle
project, parts 1 & 2][ruby-koans] for more information.

An _equilateral_ triangle has all three sides the same length.

An _isosceles_ triangle has at least two sides the same length. (It is sometimes
specified as having exactly two sides the same length, but for the purposes of
this exercise we'll say at least two.)

A _scalene_ triangle has all sides of different lengths.

## Task

In a file called `triangle.py`, implement a program that determines whether a
triangle is equilateral, isosceles, or scalene. The program should include the
following functions:

- `is_equilateral` that takes a list of floating-point values (_the side
  lengths_) as arguments and returns a Boolean value (_True if the side lengths
  make a equilateral triangle, False otherwise_).
- `is_isosceles` that takes a list of floating-point values (_the side lengths_)
  as arguments and returns a Boolean value (_True if the side lengths make an
  isosceles triangle, False otherwise_).
- `is_scalene` that takes a list of floating-point values (_the side lengths_)
  as arguments and returns a Boolean value (_True if the side lengths make a
  scalene triangle, False otherwise_).

### Testing

In a file called `test_triangle.py`, implement a test suite that covers the
following test cases:

```python
# Verify all sides equal is equilateral.
>>> is_equilateral([2, 2, 2])
True

# Verify any side unequal is not equilateral.
>>> is_equilateral([2, 3, 2])
False

# Verify no side equal is not equilateral.
>>> is_equilateral([5, 4, 6])
False

# Verify all sides zero is not equilateral.
>>> is_equilateral([0, 0, 0])
False

# Verify all equal float sides is equilateral.
>>> is_equilateral([0, 0, 0])
True
```

[ruby-koans]: https://web.archive.org/web/20220831105330/http://rubykoans.com
[triangle-inequality]: https://en.wikipedia.org/wiki/Triangle_inequality
