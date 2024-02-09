# Currency Exchange: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [Testing](#testing)

## Introduction

Your friend plans to visit exotic countries all around the world. Sadly, your
friend's mathematics skills aren't good. They are pretty worried about being
scammed by currency exchanges during their trip - and they want you to make a
currency calculator for them.

## Task

In a file called `currency_exchange.py`, implement a program that calculates
various results related to exchanging currency. The program should include the
following functions:

- `exchange_money` that takes a floating-point number (_the amount of money to
  exchange_) and a floating-point number (_the amount of domestic currency equal
  to one unit of foreign currency_) as arguments and returns the floating-point
  value of the exchanged currency.
- `get_change` that takes a floating-point number (_the amount of money
  available to exchange_) and a floating-point number (_the amount of money that
  is exchanged_) as arguments and returns the floating-point value of the
  difference between the money available and the money that is exchanged.
- `get_value_of_bills` that takes an integer (_the value of a single bill_) and
  an integer (_the total number of bills_) as arguments and returns the integer
  value of the amount of money.
- `get_number_of_bills` that takes a floating-point number (_an amount of
  money_) and an integer (_the value of a single bill_) as arguments and returns
  the integer value of the number of bills that can be obtained from the given
  amount.
- `get_leftover_of_bills` that takes a floating-point number (_an amount of
  money_) and an integer (_the value of a single bill_) as arguments and returns
  a floating-point integer (_the amount that is left over, given the
  denomination_).
- `exchangeable_value` that takes a floating-point number (_the amount to be
  exchanged_), a floating-point number (_the exchange rate_),an integer (_the
  percentage that is taken as a fee_), and an integer (_the value of a single
  bill_) as arguments and returns an integer (_the maximum value of the new
  currency after calculating the exchange rate plus the spread_).

### Testing

In a file called `test_currency_exchange.py`, implement a test suite that covers
the following test cases:

```python
# Ensure that `exchange_money` returns correctly.
>>> exchange_money(127.5, 1.2)
106.25

# Ensure that `get_change` returns correctly.
>>> get_change(127.5, 120)
7.5

# Ensure that `get_value_of_bills` returns correctly.
>>> get_value_of_bills(5, 128)
640

# Ensure that `get_number_of_bills` returns correctly.
>>> get_number_of_bills(127.5, 5)
25

# Ensure that `get_leftover_of_bills` returns correctly.
>>> get_leftover_of_bills(127.5, 20)
7.5

# Ensure that `exchangeable_value` returns correctly.
>>> exchangeable_value(127.25, 1.20, 10, 20)
80
```
