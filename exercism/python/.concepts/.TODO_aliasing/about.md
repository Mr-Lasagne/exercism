# Aliasing: About

In Python, aliasing refers to the practice of creating multiple references
(aliases) to the same object in memory. When you assign one variable to another,
both variables refer to the same underlying object. This can lead to unexpected
behavior if you're not aware of how aliasing works.

Here's a simple example of aliasing in Python:

```python
list1 = [1, 2, 3]
list2 = list1  # creating an alias

print(list1)  # [1, 2, 3]
print(list2)  # [1, 2, 3]

# Modify the original list through one of the aliases
list2.append(4)

print(list1)  # [1, 2, 3, 4]
print(list2)  # [1, 2, 3, 4]
```

In this example, `list1` and `list2` are aliases—they reference the same list
object in memory. When we modify the list through either alias, the changes are
reflected in both aliases because they point to the same underlying object.

To avoid unintended aliasing, you can use methods like `copy()` or `list()` to
create a new object with the same values:

```python
list1 = [1, 2, 3]
list2 = list(list1)  # creating a new list

print(list1)  # [1, 2, 3]
print(list2)  # [1, 2, 3]

# Modify the new list without affecting the original list
list2.append(4)

print(list1)  # [1, 2, 3]
print(list2)  # [1, 2, 3, 4]
```

Now, modifying `list2` does not affect `list1` because they are separate objects
in memory.

Understanding aliasing is important in Python programming to avoid unexpected
side effects when working with mutable objects like lists, dictionaries, or
user-defined classes.
