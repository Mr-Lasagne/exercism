# Card Games: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [1. Tracking Poker Rounds](#1-tracking-poker-rounds)
  - [2. Keeping all Rounds in the Same Place](#2-keeping-all-rounds-in-the-same-place)
  - [3. Finding Prior Rounds](#3-finding-prior-rounds)
  - [4. Averaging Card Values](#4-averaging-card-values)
  - [5. Alternate Averages](#5-alternate-averages)
  - [6. More Averaging Techniques](#6-more-averaging-techniques)
  - [7. Bonus Round Rules](#7-bonus-round-rules)
  - [Testing](#testing)

## Introduction

Elyse is really looking forward to playing some poker (and other card games)
during her upcoming trip to Vegas. Being a big fan of "self-tracking" she wants
to put together some small functions that will help her with tracking tasks and
has asked for your help thinking them through.

## Task

In a file called `card_games.py`, implement a program that calculates various
results related to card games. The program should include the following
functions:

### 1. Tracking Poker Rounds

Elyse is especially fond of poker, and wants to track how many rounds she
plays - and _which rounds_ those are. Every round has its own number, and every
table shows the round number currently being played. Elyse chooses a table and
sits down to play her first round. She plans on playing three rounds.

Implement a function `get_rounds(<round_number>)` that takes the current round
number and returns a single `list` with that round and the _next two_ that are
coming up:

### 2. Keeping all Rounds in the Same Place

Elyse played a few rounds at the first table, then took a break and played some
more rounds at a second table ... but ended up with a different list for each
table! She wants to put the two lists together, so she can track all of the
poker rounds in the same place.

Implement a function `concatenate_rounds(<rounds_1>, <rounds_2>)` that takes two
lists and returns a single `list` consisting of all the rounds in the first
`list`, followed by all the rounds in the second `list`:

### 3. Finding Prior Rounds

Talking about some of the prior Poker rounds, another player remarks how
similarly two of them played out. Elyse is not sure if she played those rounds
or not.

Implement a function `list_contains_round(<rounds>, <round_number>)` that takes
two arguments, a list of rounds played and a round number. The function will
return `True` if the round is in the list of rounds played, `False` if not:

### 4. Averaging Card Values

Elyse wants to try out a new game called Black Joe. It's similar to Black Jack -
where your goal is to have the cards in your hand add up to a target value - but
in Black Joe the goal is to get the _average_ of the card values to be 7. The
average can be found by summing up all the card values and then dividing that
sum by the number of cards in the hand.

Implement a function `card_average(<hand>)` that will return the average value
of a hand of Black Joe.

### 5. Alternate Averages

In Black Joe, speed is important. Elyse is going to try and find a faster way of
finding the average.

She has thought of two ways of getting an _average-like_ number:

- Take the average of the _first_ and _last_ number in the hand.
- Using the median (middle card) of the hand.

Implement the function `approx_average_is_average(<hand>)`, given `hand`, a list
containing the values of the cards in your hand.

Return `True` if either _one_ `or` _both_ of the, above named, strategies result
in a number _equal_ to the _actual average_.

Note: _The length of all hands are odd, to make finding a median easier._

### 6. More Averaging Techniques

Intrigued by the results of her averaging experiment, Elyse is wondering if
taking the average of the cards at the _even_ positions versus the average of
the cards at the _odd_ positions would give the same results. Time for another
test function!

Implement a function `average_even_is_average_odd(<hand>)` that returns a
Boolean indicating if the average of the cards at even indexes is the same as
the average of the cards at odd indexes.

### 7. Bonus Round Rules

Every 11th hand in Black Joe is a bonus hand with a bonus rule: if the last card
you draw is a Jack, you double its value.

Implement a function `maybe_double_last(<hand>)` that takes a hand and checks if
the last card is a Jack (11). If the last card **is** a Jack (11), double its
value before returning the hand.

### Testing

In a file called `test_card_games.py`, implement a test suite that covers the
following test cases:

```python
# Ensure that `get_rounds` returns correctly.
>>> get_rounds(27)
[27, 28, 29]

# Ensure that `concatenate_rounds` returns correctly.
>>> concatenate_rounds([27, 28, 29], [35, 36])
[27, 28, 29, 35, 36]

# Ensure that `list_contains_round` returns correctly.
>>> list_contains_round([27, 28, 29, 35, 36], 29)
True
>>> list_contains_round([27, 28, 29, 35, 36], 30)
False

# Ensure that `card_average` returns correctly.
>>> card_average([5, 6, 7])
6.0

# Ensure that `approx_average_is_average` returns correctly.
>>> approx_average_is_average([1, 2, 3])
True
>>> approx_average_is_average([2, 3, 4, 8, 8])
True
>>> approx_average_is_average([1, 2, 3, 5, 9])
False

# Ensure that `average_even_is_average_odd` returns correctly.
>>> average_even_is_average_odd([1, 2, 3])
True
>>> average_even_is_average_odd([1, 2, 3, 4])
False

# Ensure that `maybe_double_last` returns correctly.
>>> maybe_double_last([5, 9, 11])
[5, 9, 22]
>>> maybe_double_last([5, 9, 10])
[5, 9, 10]
```
