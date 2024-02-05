# Functools <!-- omit in toc -->

- [Memoizing the Function Calls](#memoizing-the-function-calls)
  - [`@functools.lru_cache(maxsize=128, typed=False)`](#functoolslru_cachemaxsize128-typedfalse)
  - [`@functools.cache(user_function)`](#functoolscacheuser_function)
- [Generic Functions](#generic-functions)
- [Partial](#partial)
- [Wraps](#wraps)
  - [`functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`](#functoolsupdate_wrapperwrapper-wrapped-assignedwrapper_assignments-updatedwrapper_updates)
  - [`functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`](#functoolswrapswrapped-assignedwrapper_assignments-updatedwrapper_updates)

The functools module is for higher-order functions: functions that act on or
return other **_[functions][defining-functions]_**. It provides functions for
working with other functions and callable objects to use or extend them without
completely rewriting them.

## Memoizing the Function Calls

**Memoizing:** Storing the result of some expensive function, which is called
with the same input again and again. So, we don't have to run the function
repeatedly.

### `@functools.lru_cache(maxsize=128, typed=False)`

**_[@functools.lru_cache(maxsize=128, typed=False)][functools-lru-cache]_**
Decorator to wrap a function with a memoizing callable that saves up to the
maxsize most recent calls. It can save time when an expensive or I/O bound
function is periodically called with the same arguments.

Since a dictionary is used to cache results, the positional and keyword
arguments to the function must be hashable.

Here `maxsize = 128` means that it is going to memoize latest 128 function calls
at max.

### `@functools.cache(user_function)`

**_[@functools.cache(user_function)][functools-cache]_** the same as
lru_cache(maxsize=None), creating a thin wrapper around a dictionary lookup for
the function arguments. Because it never needs to evict old values, this is
smaller and faster than `lru_cache()` with a size limit.

## Generic Functions

**_[Generic functions][generic-functions]_** are those which preform the
operation based on the argument given to them.

In statically typed languages it can be done by function overloading, In python
functools provides the `singledispatch(func)` decorator to register a set of
generic functions for automatic switching based on the type of the first
argument to a function.

For class methods we can use
**_[singledispatchmethod(func)][singledispatchmethod]_** to register a set of
generic methods for automatic switching based on the type of the first non-self
or non-class argument to a function.

## Partial

`functools.partial(func, /, *args, **keywords)` return a new **_[partial
object][partial-objects]_** which when called will behave like func called with
the positional arguments args and keyword arguments keywords. If more arguments
are supplied to the call, they are appended to args.The
**_[partial][functools-partial]_** is used for partial function application
which “freezes” some portion of a function’s arguments and/or keywords resulting
in a new object with a simplified signature.

***[functools.partialmethod(func, /, *args,
**keywords)][functools-partialmethod]\*\*\* Return a new partialmethod
descriptor which behaves like partial except that it is designed to be used as a
method definition rather than being directly callable.

## Wraps

### `functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`

**_[functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS,
updated=WRAPPER_UPDATES)][functools-update-wrapper]_** Update a wrapper function
to look like the wrapped function. The optional arguments are tuples to specify
which attributes of the original function are assigned directly to the matching
attributes on the wrapper function and which attributes of the wrapper function
are updated with the corresponding attributes from the original function.

### `functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`

**_[functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS,
updated=WRAPPER_UPDATES)][functools-wraps]_** is a convenience function for
invoking update_wrapper() as a function decorator when defining a wrapper
function. It is equivalent to partial(update_wrapper, wrapped=wrapped,
assigned=assigned, updated=updated).

[defining-functions]:
  https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[functools-cache]:
  https://docs.python.org/3/library/functools.html#functools.cache
[functools-lru-cache]:
  https://docs.python.org/3/library/functools.html#functools.lru_cache
[functools-partial]:
  https://docs.python.org/3/library/functools.html#functools.partial
[functools-partialmethod]:
  https://docs.python.org/3/library/functools.html#functools.partialmethod
[functools-update-wrapper]:
  https://docs.python.org/3/library/functools.html#functools.update_wrapper
[functools-wraps]:
  https://docs.python.org/3/library/functools.html#functools.wraps
[generic-functions]: https://pymotw.com/3/functools/#generic-functions
[partial-objects]:
  https://docs.python.org/3/library/functools.html#partial-objects
[singledispatchmethod]:
  https://docs.python.org/3/library/functools.html#functools.singledispatchmethod
