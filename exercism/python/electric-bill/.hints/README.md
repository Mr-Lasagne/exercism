# Electric Bill: Hints

- [1. Get extra hours](#1-get-extra-hours)
- [2. Get kW value](#2-get-kw-value)
- [3. Get kwh value](#3-get-kwh-value)
- [4. Get efficiency](#4-get-efficiency)
- [5. Get cost](#5-get-cost)

Remember that you can always reuse/call previously completed functions when
writing new ones.

## 1. Get extra hours

- This is all about calculating the _remainder_ left after whole division.
- Take a look at [`divmod()`][divmod], and look for an operator that does
  something similar.

## 2. Get kW value

- Remember to give [`round()`][round] a number of _decimal places_, or you will
  get a whole number back as a result.

## 3. Get kwh value

- The result of dividing an `int` by a `float` is always a `float`.
- To get only an integer value from division, use [_floor_ division][floor],
  which will truncate the decimal.

## 4. Get efficiency

- The result of dividing an `int` by a `float` is always a `float`.

## 5. Get cost

- It might be good to _reuse_ or call other functions you have already completed
  here.
- The result of dividing an `int` by a `float` is always a `float`.

[divmod]: https://docs.python.org/3/library/functions.html#divmod
[floor]: https://docs.python.org/3/glossary.html#term-floor-division
[round]: https://docs.python.org/3/library/functions.html#round
