import builtins
import functools

__all__ = (
  "curry", "compose", "pipe",
  "T", "F", "identity", "always", "alternation", "tap", "fork",
  "reduce", "map", "filter", "take", "flatten", "flatmap", "groupby",
  "includes", "pluck",
  "prop", "propeq", "propis",
  "cond", "defaultto",
)

# Function
def curry(f, wargs=[], wkwargs={}):
  @functools.wraps(f)
  def wrapper(*nargs, **nkwargs):
    args = wargs + list(nargs)
    kwargs = {**nkwargs, **nkwargs}
    arity = f.__code__.co_argcount
    if len(args) + len(kwargs) >= arity:
      return f(*args, **kwargs)
    return curry(f, args)
  return wrapper


def _compose2(f, g):
  return lambda *args: f(g(*args))

def compose(*fns):
  """
  >>> add3 = lambda x: x + 3
  >>> mul2 = lambda x: x * 2
  >>> square = lambda x: x * x
  >>> pipe(add3, mul2, square)(1)
  5
  """
  return functools.reduce(_compose2, fns)

def _pipe2(f, g):
  return lambda *args: g(f(*args))

def pipe(*fns):
  """
  >>> add3 = lambda x: x + 3
  >>> mul2 = lambda x: x * 2
  >>> square = lambda x: x * x
  >>> pipe(add3, mul2, square)(1)
  64
  """
  return functools.reduce(_pipe2, fns)

def T(*args):
  return True

def F(*args):
  return False

def memomize(f):
  cache = {}
  def _(*nargs, **nkwargs):
    pass

"""
Function Combinators
"""
def identity(x):
  """
  >>> identity(42)
  42
  """
  return x

def always(x):
  """
  >>> always(42)()
  42
  """
  return lambda *args, **kwargs: x

@curry
def alternation(f1, f2, x):
  f1_result = f1(x)
  return f1_result if f1_result else f2(x)

@curry
def tap(f, x):
  """
  >>> log = tap(print)
  >>> log(10)
  10
  10
  """
  f(x)
  return x

@curry
def fork(fns, joiner, x):
  results = map(lambda f: f(x), fns)
  return joiner(*results)

"""
Iterator
"""
@curry
def reduce(initial, reducer, xs):
  return functools.reduce(reducer, xs, initial)

@curry
def map(f, xs):
  """
  >>> addOne = lambda x: x + 1
  >>> map(addOne, [1, 2, 3, 4])
  [2, 3, 4, 5]

  >>> class Functor():
  >>>   def __init__(v):
  >>>     self.v = v
  >>>   def fmap(self, f):
  >>>     return Functor(f(self.v))
  >>> map(lambda x: x * 3)(Functor(14)).v
  42
  """

  if hasattr(xs, "fmap"):
    return xs.fmap(f)
  return list(builtins.map(f, xs))

@curry
def filter(pred, xs):
  """
  >>> iseven = lambda x: x % 2 == 0
  >>> filter(iseven, [1, 2, 3, 4, 5, 6, 7])
  [2, 4, 6]
  """
  return list(builtins.filter(pred, xs))

@curry
def take(number, xs):
  """
  >>> take3 = take(3)
  >>> take3([1, 2, 3, 4, 5, 6, 7])
  [1, 2, 3]
  """
  if number > len(xs):
    return xs
  return [xs[i] for i in range(0, number)]

def flatten(xs):
  """ flatten an array
  >>> flatten([[1, 2], [3, 4]])
  [1, 2, 3, 4]
  """
  return functools.reduce(lambda acc, v: [*acc, *v], xs, [])

@curry
def flatmap(f, xs):
  """ map and flatten an array (= flatten(map(f)))
  >>> flatmap(lambda x: [2 * x], [1, 2, 3, 4])
  [2, 4, 6, 8]
  """
  return compose(
    flatten,
    map(f),
  )(xs)

@curry
def pluck(key, xs):
  """
  >>> pluck_age = pluck("age")
  >>> pluck_age([
    {"name": "Alice", "age": 30},
    {"name": "John", "age": 42},
    {"name": "Eve", "age": 34},
  ])
  [30, 42, 34]
  """
  return map(prop(key), xs)

@curry
def includes(xs: list, x):
  return x in xs

@curry
def groupby(key, xs):
  """ Group a list by a key or a classifier function
  from ftool import groupby
  >>> groupby("gender", [{"gender": "M", "name": "John"}, {"gender": "F", "name": "Alice"}, {"gender": "M", "name": "N"}])
  {'M': [{'gender': 'M', 'name': 'John'}, {'gender': 'M', 'name': 'N'}], 'F': [{'gender': 'F', 'name': 'Alice'}]}

  >>> iseven = lambda x: x % 2 == 0
  >>> groupby(iseven, [1, 2, 3, 4, 5, 6, 7, 8])
  {False: [1, 3, 5, 7], True: [2, 4, 6, 8]}
  """
  classify = key if callable(key) else lambda x: x[key]
  d = {}
  for x in xs:
    k = classify(x)
    l = d.get(k, [])
    l.append(x)
    d[k] = l
  return d

"""
Dict
"""
@curry
def prop(name, o):
  """
  >>> get_name = prop("name")
  >>> a = {"prop1": "value1", "name": "John"}
  >>> get_name(a)
  'John'
  """
  if isinstance(o, dict):
    return o[name]
  return getattr(o, name, None)

"""
Logic
"""
def cond(pairs):
  """ Returns a function which encapsulates 'if/else', 'if/else' ... logic
  >>> lt30 = lambda num: num < 30
  >>> lt60 = lambda num: num < 60
  >>> lt85 = lambda num: num < 85
  >>>
  >>> f = cond([
    [lt30, "D"],
    [lt60, "C"],
    [lt85, "B"],
    [T, "A"],
  ])
  >>> f(0)
  'D'
  >>> f(90)
  'A'

  """
  def f(x):
    for predicate, transformer in pairs:
      if predicate(x):
        return transformer(x) if callable(transformer) else transformer
  return f

@curry
def defaultto(default, x):
  return x if x else default

@curry
def propeq(key, expected, o):
  """objectの属性またはdictのキーに対する値が指定された値と等しいかを検証します
  """
  return prop(key, o) == expected

@curry
def propis(key, expected, o):
  """objectの属性またはdictのキーに対する値が一致するかを検証します
  """
  return prop(key, o) is expected

"""
Heigher level function
"""
@tap
def log(x: str):
  print(x)
