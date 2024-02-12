# Making the Grade: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [1. Rounding Scores](#1-rounding-scores)
  - [2. Non-Passing Students](#2-non-passing-students)
  - [3. The "Best"](#3-the-best)
  - [4. Calculating Letter Grades](#4-calculating-letter-grades)
  - [5. Matching Names to Scores](#5-matching-names-to-scores)
  - [6. A "Perfect" Score](#6-a-perfect-score)
  - [Testing](#testing)

## Introduction

You're a teaching assistant correcting student exams. Keeping track of results
manually is getting both tedious and mistake-prone. You decide to make things a
little more interesting by putting together some functions to count and
calculate results for the class.

## Task

In a file called `making_the_grade.py`, implement a program that calculates
various results related to keeping track of exam results. The program should
include the following functions:

### 1. Rounding Scores

While you can give "partial credit" on exam questions, overall exam scores have
to be `int`s. So before you can do anything else with the class scores, you need
to go through the grades and turn any `float` scores into `int`s. Lucky for you,
Python has the built-in [`round()`][round] function you can use.

Create the function `round_scores(student_scores)` that takes a `list` of
`student_scores`. This function should _consume_ the input `list` and `return` a
new list with all the scores converted to `int`s. The order of the scores in the
resulting `list` is not important.

### 2. Non-Passing Students

As you were grading the exam, you noticed some students weren't performing as
well as you had hoped. But you were distracted, and forgot to note exactly _how
many_ students.

Create the function `count_failed_students(student_scores)` that takes a `list`
of `student_scores`. This function should count up the number of students who
don't have passing scores and return that count as an integer. A student needs a
score greater than **40** to achieve a passing grade on the exam.

### 3. The "Best"

The teacher you're assisting wants to find the group of students who've
performed "the best" on this exam. What qualifies as "the best" fluctuates, so
you need to find the student scores that are **greater than or equal to** the
current threshold.

Create the function `above_threshold(student_scores, threshold)` taking
`student_scores` (a `list` of grades), and `threshold` (the "top score"
threshold) as parameters. This function should return a `list` of all scores
that are `>=` to `threshold`.

### 4. Calculating Letter Grades

The teacher you are assisting likes to assign letter grades as well as numeric
scores. Since students rarely score 100 on an exam, the "letter grade" lower
thresholds are calculated based on the highest score achieved, and increment
evenly between the high score and the failing threshold of **<= 40**.

Create the function `letter_grades(highest)` that takes the "highest" score on
the exam as an argument, and returns a `list` of lower score thresholds for each
"American style" grade interval: `["D", "C", "B", "A"]`.

### 5. Matching Names to Scores

You have a list of exam scores in descending order, and another list of student
names also sorted in descending order by their exam scores. You would like to
match each student name with their exam score and print out an overall class
ranking.

Create the function `student_ranking(student_scores, student_names)` with
parameters `student_scores` and `student_names`. Match each student name on the
student_names `list` with their score from the student_scores `list`. You can
assume each argument `list` will be sorted from highest score(er) to lowest
score(er). The function should return a `list` of strings with the format
`<rank>. <student name>: <student score>`.

### 6. A "Perfect" Score

Although a "perfect" score of 100 is rare on an exam, it is interesting to know
if at least one student has achieved it.

Create the function `perfect_score(student_info)` with parameter `student_info`.
`student_info` is a `list` of lists containing the name and score of each
student: `[["Charles", 90], ["Tony", 80]]`. The function should `return` _the
first_ `[<name>, <score>]` pair of the student who scored 100 on the exam.

If no 100 scores are found in `student_info`, an empty list `[]` should be
returned.

[round]: https://docs.python.org/3/library/functions.html#round

### Testing

In a file called `test_making_the_grade.py`, implement a test suite that covers
the following test cases:

```python
# Ensure that `round_scores` returns correctly.
>>> round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])
[40, 39, 95, 80, 25, 31, 70, 55, 40, 90]

# Ensure that `count_failed_students` returns correctly.
>>> count_failed_students([90, 40, 55, 70, 30, 25, 80, 95, 38, 40])
5

# Ensure that `above_threshold` returns correctly.
>>> above_threshold([90, 40, 55, 70, 30, 68, 70, 75, 83, 96], 75)
[90, 75, 83, 96]

# Ensure that `letter_grades` returns correctly.
>>> letter_grades(100)
[41, 56, 71, 86]
>>> letter_grades(88)
[41, 53, 65, 77]

# Ensure that `student_ranking` returns correctly.
>>> student_ranking([100, 99, 90, 84, 66], ['Joci', 'Sara', 'Kora', 'Jan', 'John'])
['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66']

# Ensure that `perfect_score` returns correctly.
>>> perfect_score([["Charles", 90], ["Tony", 80], ["Alex", 100]])
["Alex", 100]
>>> perfect_score([["Charles", 90], ["Tony", 80]])
[]
```
