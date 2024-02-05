# Simple Linked List: Hints

- [General](#general)

## General

- This challenge is about creating a [_stack_][stack-data-structure] using a
  [singly linked list][linked-list].
- Unlike stacks underpinned with `lists`, `collections.deque`, or
  `queue.LifoQueue`, we ask you create custom `Node` and `LinkedList`
  [`classes`][tut-classes] to store and link elements.

![Diagram representing a stack implemented with a linked list. A circle with a dashed border named New_Node is to the far left-hand side, with two dotted arrow lines pointing right-ward.  New_Node reads "(becomes head) - New_Node - next = node_6". The top dotted arrow line is labeled "push" and points to Node_6, above and to the right.  Node_6 reads "(current) head - Node_6 - next = node_5". The bottom dotted arrow line is labeled "pop" and points to a box that reads "gets removed on pop()". Node_6 has a solid arrow that points rightward to Node_5, which reads "Node_5 - next = node_4". Node_5 has a solid arrow pointing rightward to Node_4, which reads "Node_4 - next = node_3". This pattern continues until Node_1, which reads "(current) tail - Node_1 - next = None". Node_1 has a dotted arrow pointing rightward to a node that says "None".](https://assets.exercism.org/images/tracks/python/simple-linked-list/linked-list.svg)

- [Real Python: Linked Lists][realpython-linked-lists], [Towards Data Science:
  Demystifying the Linked List][demystifying-linked-list], and [ADS Stack in
  Python][koderdojo-linked-list] can be helpful to review for details on
  implementation.
- Your `LinkedList` should accept a `list` argument to its _constructor_, but
  should not use a `list` to store nodes or elements.
- `len()` is a built-in function for most Python objects. In order for _custom
  objects_ to support `len()`, the special method [`__len__`][len] needs to be
  defined.
- Iteration in Python is supported for most sequence, container, or collection
  type objects. In order for a _custom_ object to support looping or
  re-ordering, the special method `__iter__` needs to be defined. [Implementing
  an iterator for a class.][iterators] can help show you how.

[stack-data-structure]: https://www.baeldung.com/cs/stack-data-structure
[koderdojo-linked-list]:
  https://www.koderdojo.com/blog/coding-a-stack-abstract-data-structure-using-linked-list-in-python
[realpython-linked-lists]: https://realpython.com/linked-lists-python/
[len]: https://docs.python.org/3/reference/datamodel.html#object.__len__
[tut-classes]: https://docs.python.org/3/tutorial/classes.html#tut-classes
[iterators]: https://docs.python.org/3/tutorial/classes.html#iterators
[linked-list]: https://towardsdatascience.com/python-linked-lists-c3622205da81
[demystifying-linked-list]:
  https://towardsdatascience.com/demystifying-linked-list-258dfb9f2176
