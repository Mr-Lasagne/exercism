# Chaitana's Colossal Coaster: Hints

- [1. Add Me to the queue](#1-add-me-to-the-queue)
- [2. Where are my friends](#2-where-are-my-friends)
- [3. Can I please join them?](#3-can-i-please-join-them)
- [4. Mean person in the queue](#4-mean-person-in-the-queue)
- [5. Namefellows](#5-namefellows)
- [6. Remove the last person](#6-remove-the-last-person)
- [7. Sort the Queue List](#7-sort-the-queue-list)

## 1. Add Me to the queue

- An `if-else` statement can help you find which ticket type you are dealing
  with.
- You can then `append()` the person to the queue based on the ticket type.

## 2. Where are my friends

- You need to find the `index()` of the friend name from the queue.

## 3. Can I please join them?

- Since you know the `index()`, you can `insert()` the friend into the queue at
  that point.

## 4. Mean person in the queue

- You know the mean persons name, so you can `remove()` them from the queue.

## 5. Namefellows

- `count()`-ing the occurrences of the `name` in the queue could be a good
  strategy here.

## 6. Remove the last person

- Although you could `remove()` the person by name, `pop()`-ing them out might
  be quicker.

## 7. Sort the Queue List

- Don't forget that You need to avoid mutating the queue and losing its original
  order.
- Once you have a `copy()`, `sort()`-ing should be straightforward.
- We're looking for an _ascending_ sort, or _alphabetical from a-z_.
