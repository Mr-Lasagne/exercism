# Chaitana's Colossal Coaster: Instructions

- [Introduction](#introduction)
- [Task](#task)
  - [1. Add me to the queue](#1-add-me-to-the-queue)
  - [2. Where are my friends?](#2-where-are-my-friends)
  - [3. Can I please join them?](#3-can-i-please-join-them)
  - [4. Mean person in the queue](#4-mean-person-in-the-queue)
  - [5. Namefellows](#5-namefellows)
  - [6. Remove the last person](#6-remove-the-last-person)
  - [7. Sort the Queue List](#7-sort-the-queue-list)
  - [Testing](#testing)

## Introduction

Chaitana owns a very popular theme park. She only has one ride in the very
center of beautifully landscaped grounds: The Biggest Roller Coaster in the
World(TM). Although there is only this one attraction, people travel from all
over the world and stand in line for hours for the opportunity to ride
Chaitana's hypercoaster.

There are two queues for this ride, each represented as a `list`:

1. Normal Queue
2. Express Queue (_also known as the Fast-track_) - where people pay extra for
   priority access.

You have been asked to write some code to better manage the guests at the park.
You need to implement the following functions as soon as possible before the
guests (and your boss, Chaitana!) get cranky.

## Task

In a file called `chaitanas_colossal_coaster.py`, implement a program that
calculates various results related to queue management. The program should
include the following functions:

### 1. Add me to the queue

Define the `add_me_to_the_queue()` function that takes 4 parameters
`<express_queue>, <normal_queue>, <ticket_type>, <person_name>` and returns the
appropriate queue updated with the person's name.

1. `<ticket_type>` is an `int` with 1 == express_queue and 0 == normal_queue.
2. `<person_name>` is the name (as a `str`) of the person to be added to the
   respective queue.

### 2. Where are my friends?

One person arrived late at the park but wants to join the queue where their
friends are waiting. But they have no idea where their friends are standing and
there isn't any phone reception to call them.

Define the `find_my_friend()` function that takes 2 parameters `queue` and
`friend_name` and returns the position in the queue of the person's name.

1. `<queue>` is the `list` of people standing in the queue.
2. `<friend_name>` is the name of the friend whose index (place in the queue)
   you need to find.

Remember: Indexing starts at 0 from the left, and -1 from the right.

### 3. Can I please join them?

Now that their friends have been found (in task #2 above), the late arriver
would like to join them at their place in the queue. Define the
`add_me_with_my_friends()` function that takes 3 parameters `queue`, `index`,
and `person_name`.

1. `<queue>` is the `list` of people standing in the queue.
2. `<index>` is the position at which the new person should be added.
3. `<person_name>` is the name of the person to add at the index position.

Return the queue updated with the late arrivals name.

### 4. Mean person in the queue

You just heard from the queue that there is a really mean person shoving,
shouting, and making trouble. You need to throw that miscreant out for bad
behavior!

Define the `remove_the_mean_person()` function that takes 2 parameters `queue`
and `person_name`.

1. `<queue>` is the `list` of people standing in the queue.
2. `<person_name>` is the name of the person that needs to be kicked out.

Return the queue updated without the mean person's name.

### 5. Namefellows

You may not have seen two unrelated people who look exactly the same, but you
have _definitely_ seen unrelated people with the exact same name
(_namefellows_)! Today, it looks like there are a lot of them in attendance. You
want to know how many times a particular name occurs in the queue.

Define the `how_many_namefellows()` function that takes 2 parameters `queue` and
`person_name`.

1. `<queue>` is the `list` of people standing in the queue.
2. `<person_name>` is the name you think might occur more than once in the
   queue.

Return the number of occurrences of `person_name`, as an `int`.

### 6. Remove the last person

Sadly, it's overcrowded at the park today and you need to remove the last person
in the normal line (_you will give them a voucher to come back in the fast-track
on another day_). You will have to define the function
`remove_the_last_person()` that takes 1 parameter `queue`, which is the list of
people standing in the queue.

You should update the `list` and also `return` the name of the person who was
removed, so you can write them a voucher.

### 7. Sort the Queue List

For administrative purposes, you need to get all the names in a given queue in
alphabetical order.

Define the `sorted_names()` function that takes 1 argument, `queue`, (the `list`
of people standing in the queue), and returns a `sorted` copy of the `list`.

### Testing

In a file called `test_chaitanas_colossal_coaster.py`, implement a test suite
that covers the following test cases:

```python
# Ensure that `add_me_to_the_queue` returns correctly.
>>> add_me_to_the_queue(["Tony", "Bruce"], ["RobotGuy", "WW"], 1, "RichieRich")
['Tony', 'Bruce', 'RichieRich']
>>> add_me_to_the_queue(["Tony", "Bruce"], ["RobotGuy", "WW"], 0, "HawkEye")
['RobotGuy', 'WW', 'HawkEye']

# Ensure that `find_my_friend` returns correctly.
>>> find_my_friend(["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], "Steve")
1

# Ensure that `add_me_with_my_friends` returns correctly.
>>> add_me_with_my_friends(["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], 1, "Bucky")
["Natasha", "Bucky", "Steve", "T'challa", "Wanda", "Rocket"]

# Ensure that `remove_the_mean_person` returns correctly.
>>> remove_the_mean_person(["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], "Eltran")
['Natasha', 'Steve', 'Wanda', 'Rocket']

# Ensure that `how_many_namefellows` returns correctly.
>>> how_many_namefellows(["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], "Natasha")
2

# Ensure that `remove_the_last_person` returns correctly.
>>> remove_the_last_person(["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
'Rocket'

# Ensure that `sorted_names` returns correctly.
>>> sorted_names(["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
['Eltran', 'Natasha', 'Natasha', 'Rocket', 'Steve']
```
