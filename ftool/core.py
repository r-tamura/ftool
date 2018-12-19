import builtins
import collections
import functools

__all__ = (
  "curry", "compose",
  "always", "identity",
  "map", "flatten", "flatmap",
)

"""
Function
"""
def curry(f, wargs = (), wkwargs = {}):
  @functools.wraps(f)
  def wrapper(*nargs, **nkwargs):
    args = wargs + nargs
    kwargs = {**wkwargs, **nkwargs}
    arity = f.__code__.co_argcount
    if len(args) + len(kwargs) >= arity:
      return f(*args, **kwargs)
    return curry(f, args, kwargs)
  return wrapper

def compose(*fns):
  compose2 = lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs))
  return functools.reduce(compose2, fns)

def always(x):
  """
  a -> (* -> a)
  >>> always(42)()
  42
  """
  return lambda: x

def identity(x):
  """
  a -> a
  >>> identity(42)
  42
  """
  return x

"""
Iterator
"""
@curry
def map(f, xs):
  """
  >>> map(lambda x: x * 2, [1, 2, 3])
  [2, 4, 6]
  """
  return list(builtins.map(f, xs))

def flatten(xs):
  """
  [a] -> [b]
  >>> flatten([[1, 2], [3, 4]])
  [1, 2, 3, 4]
  """
  return functools.reduce(lambda acc, v: acc + v, xs)

@curry
def flatmap(f, xs):
  """
  >>> flatmap(lambda x: [x * 2], [1, 2, 3])
  [2, 4, 6]
  """
  return compose(
    flatten,
    map(f),
  )(xs)
