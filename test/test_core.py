from ftool import (
  curry, compose,
  always, identity,
  map, flatten, flatmap,
)

def test_curry():
  f = lambda x, y, z: x + y + z
  assert curry(f)(1, 2, 39) == 42
  assert curry(f)(1, 2)(39) == 42
  assert curry(f)(1)(2)(39) == 42

def test_compose():
  assert compose(
    lambda x: x + 2,
    lambda x: x * 2,
    lambda a, b: a + b
  )(15, 5) == 42, "not 42"

  assert compose(
    lambda x: x + 2,
    lambda x: x * 2,
    lambda a=0, b=0: a + b
  )(b=5, a=15) == 42

def test_always():
  assert always(42)() == 42

def test_identity():
  assert identity(42) == 42

def test_map():
  assert map(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]

def test_flatten():
  assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_flatmap():
  assert flatmap(lambda x: [x * 2], [1, 2, 3]) == [2, 4, 6]

