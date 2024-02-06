# Guido's Gorgeous Lasagna: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [Testing](#testing)

## Introduction

You're going to write some code to help you cook a gorgeous lasagna from your
favorite cookbook.

## Task

In a file called `guidos_gorgeous_lasagna.py`, implement a program that
calculates various time-related aspects of cooking a lasagna. The program should
include the following functions:

- `bake_time_remaining` that takes an integer `time` (_how many minutes the
  lasagna has been in the oven_) as an argument and returns how many minutes the
  lasagna still needs to bake (_note that the lasagna has a total bake time of
  40 minutes_).
- `total_layer_preparation_time` that takes an integer `number_of_layers` (_the
  number of layers in the lasagna_) as an argument and returns how many minutes
  you would spend making them (_note that each layer takes 2 minutes to
  prepare_).
- `total_elapsed_cooking_time` that takes an integer `number_of_layers` (_the
  number of layers in the lasagna_) and an integer `elapsed_bake_time` (_the
  number of minutes the lasagna has been baking in the oven_) as arguments and
  returns the sum of the preparation time and the time the lasagna has already
  spent baking in the oven.

### Testing

In a file called `test_guidos_gorgeous_lasagna.py`, implement a test suite that
covers the following test cases:

```python
# Ensure `bake_time_remaining` returns the correct value.
>>> bake_time_remaining(30)
10

# Ensure `total_layer_preparation_time` returns the correct value.
>>> total_layer_preparation_time(2)
4

# Ensure `total_elapsed_cooking_time` returns the correct value.
>>> total_elapsed_cooking_time(3, 20)
26
```
