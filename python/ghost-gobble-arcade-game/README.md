# Ghost Gobble Arcade Game: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [Testing](#testing)

## Introduction

[Pac-Man][pac-man], originally called Puck Man in Japan, is a 1980 maze action
video game developed and released for arcades.

## Task

In a file called `ghost_gobble_arcade_game.py`, implement a program that covers
various rules of Pac-Man. The program should include the following functions:

- `can_eat_ghost` that takes a Boolean value (_does Pac-Man have a power pellet
  active?_) and a Boolean value (_is Pac-Man touching a ghost?_) as arguments
  and returns `True` if Pac-man has a power pellet active and is touching a
  ghost and `False` otherwise.
- `has_scored` that takes a Boolean value (_is Pac-Man touching a power
  pellet?_) and a Boolean value (_is Pac-Man touching a dot?_) as arguments and
  returns `True` if Pac-Man is touching a power pellet or a dot and `False`
  otherwise.
- `has_lost` that takes a Boolean value (_does Pac-Man have a power pellet
  active?_) and a Boolean value (_is Pac-Man touching a ghost?_) as arguments
  and returns `True` if Pac-Man does not have a power pellet active and is
  touching a ghost and `False` otherwise.
- `has_won` that takes a Boolean value (_has Pac-Man eaten all of the dots_), a
  Boolean value (_does Pac-Man have a power pellet active?_), and a Boolean
  value (_is Pac-Man touching a ghost?_) as arguments and returns `True` if
  Pac-Man has eaten all of the dots and has not lost according to the function
  `has_lost`.

### Testing

In a file called `test_ghost_gobble_arcade_game.py`, implement a test suite that
covers the following test cases:

```python
# Ensure `can_eat_ghost` returns the correct value.
>>> can_eat_ghost(True, True)
True
>>> can_eat_ghost(False, True)
False

# Ensure `has_scored` returns the correct value.
>>> does_score(True, True)
True
>>> does_score(False, False)
False

# Ensure `has_lost` returns the correct value.
>>> does_lose(True, True)
False
>>> does_lose(False, True)
True

# Ensure `has_won` returns the correct value.
>>> win(True, True, True)
True
>>> win(False, True, True)
False
```

[pac-man]: https://en.wikipedia.org/wiki/Pac-Man
