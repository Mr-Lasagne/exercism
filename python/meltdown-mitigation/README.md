# Meltdown Mitigation: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [1. Check for criticality](#1-check-for-criticality)
  - [2. Determine the Power output range](#2-determine-the-power-output-range)
  - [3. Fail Safe Mechanism](#3-fail-safe-mechanism)
  - [Testing](#testing)

## Introduction

You're going to develop a simple control system for a nuclear reactor.

For a reactor to produce the power it must be in a state of _criticality_. If
the reactor is in a state less than criticality, it can become damaged. If the
reactor state goes beyond criticality, it can overload and result in a meltdown.
You want to mitigate the chances of meltdown and correctly manage reactor state.

## Task

In a file called `meltdown_mitigation.py`, implement a program that covers
various aspects of a nuclear reactor control system. The program should include
the following functions:

### 1. Check for criticality

The first thing a control system has to do is check if the reactor is balanced
in criticality. A reactor is said to be critical if it satisfies the following
conditions:

- The temperature is less than 800 K.
- The number of neutrons emitted per second is greater than 500.
- The product of temperature and neutrons emitted per second is less
  than 500000.

Implement the function `is_criticality_balanced()` that takes `temperature`
measured in kelvin and `neutrons_emitted` as parameters, and returns `True` if
the criticality conditions are met, `False` if not.

### 2. Determine the Power output range

Once the reactor has started producing power its efficiency needs to be
determined. Efficiency can be grouped into 4 bands:

1. `green` -> efficiency of 80% or more,
2. `orange` -> efficiency of less than 80% but at least 60%,
3. `red` -> efficiency below 60%, but still 30% or more,
4. `black` -> less than 30% efficient.

The percentage value can be calculated as
`(generated_power/theoretical_max_power)*100` where `generated_power` =
`voltage` \* `current`. Note that the percentage value is usually not an integer
number, so make sure to consider the proper use of the `<` and `<=` comparisons.

Implement the function
`reactor_efficiency(<voltage>, <current>, <theoretical_max_power>)`, with three
parameters: `voltage`, `current`, and `theoretical_max_power`. This function
should return the efficiency band of the reactor : 'green', 'orange', 'red', or
'black'.

### 3. Fail Safe Mechanism

Your final task involves creating a fail-safe mechanism to avoid overload and
meltdown. This mechanism will determine if the reactor is below, at, or above
the ideal criticality threshold. Criticality can then be increased, decreased,
or stopped by inserting (or removing) control rods into the reactor.

Implement the function called `fail_safe()`, which takes 3 parameters:
`temperature` measured in kelvin, `neutrons_produced_per_second`, and
`threshold`, and outputs a status code for the reactor.

- If `temperature * neutrons_produced_per_second` < 90% of `threshold`, output a
  status code of 'LOW' indicating that control rods must be removed to produce
  power.

- If the value `temperature * neutrons_produced_per_second` is within 10% of the
  `threshold` (so either 0-10% less than the threshold, at the threshold, or
  0-10% greater than the threshold), the reactor is in _criticality_ and the
  status code of 'NORMAL' should be output, indicating that the reactor is in
  optimum condition and control rods are in an ideal position.

- If `temperature * neutrons_produced_per_second` is not in the above-stated
  ranges, the reactor is going into meltdown and a status code of 'DANGER' must
  be passed to immediately shut down the reactor.

### Testing

In a file called `test_meltdown_mitigation.py`, implement a test suite that
covers the following test cases:

```python
# Ensure `is_criticality_balanced` returns correctly.
>>> is_criticality_balanced(750, 600)
True

# Ensure `reactor_efficiency` returns correctly.
>>> reactor_efficiency(10, 1000, 10000)
'green'
>>> reactor_efficiency(10, 799, 10000)
'orange'
>>> reactor_efficiency(10, 599, 10000)
'red'
>>> reactor_efficiency(10, 299, 10000)
'black'

# Ensure `fail_safe` returns correctly.
>>> fail_safe(10, 399, 10000)
'LOW'
>>> fail_safe(10, 901, 10000)
'NORMAL'
>>> fail_safe(10, 1101, 10000)
'DANGER'
```
