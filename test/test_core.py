from ftool import (
  compose, pipe, curry, T, F, identity, always, alternation, fork,
  map, groupby, flatten, flatmap, pluck, includes,
  prop, cond, defaultto,
)

"""
Function
"""
def test_compose_simple():
  add = lambda x, y: x + y
  mul2 = lambda x: x * 2
  assert compose(mul2, add)(1, 2) == 6

def test_pipe_simple():
  add = lambda x, y: x + y
  mul2 = lambda x: x * 2
  assert pipe(add, mul2)(1, 2) == 6

def test_curry():
  add = curry(lambda x, y: x + y)
  mul = curry(lambda x, y: x * y)
  add3 = add(3)
  mul6 = mul(6)
  assert add3(39) == 42
  assert mul6(7) == 42

def test_t():
  assert T()

def test_f():
  assert not F()

def test_alternation():
  assert alternation(identity, F)(42) == 42
  assert alternation(F, identity)(42) == 42

def test_fork():
  f = lambda x: x + 1
  g = lambda x: x * 2
  h = lambda x: x * x
  join = lambda x, y, z: y + z - x
  assert fork([f, g, h], join)(6) == 41

"""
Iterator
"""
def test_map():
  assert map(lambda x: x)([1, 2, 3]) == [1, 2, 3]

def test_flatten():
  assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_flatmap():
  assert flatmap(lambda x: [2*x], [1, 2, 3, 4]) == [2, 4, 6, 8]

def test_groupby():
  assert groupby("gender", [
    {'name': 'Alice', 'gender': 'F'},
    {'name': 'Bob', 'gender': 'M'},
    {'name': 'Charlie', 'gender': 'M'},
  ]) == {
    "F": [{'name': 'Alice', 'gender': 'F'}],
    "M": [
      {'name': 'Bob', 'gender': 'M'},
      {'name': 'Charlie', 'gender': 'M'},
    ]
  }
  def classify(score):
    if score < 30:
      return "D"
    elif score < 60:
      return "C"
    elif score < 85:
      return "B"
    else:
      return "A"
  assert groupby(classify)([20, 60, 50, 95, 10, 45]) == {
    "A": [95], "B": [60], "C": [50, 45], "D": [20, 10]
  }

def test_pluck():
  pluck_age = pluck("age")
  assert pluck_age([
    {"name": "Alice", "age": 30},
    {"name": "John", "age": 42},
    {"name": "Eve", "age": 34},
  ]) == [30, 42, 34]

def test_includes():
  is_in_name = includes(["John", "Alice", "Eve", "Bob"])
  assert is_in_name("Eve")
  assert not is_in_name("Daniel")

"""
Logic
"""
def test_cond():
  f = cond([
    [lambda x: x < 30, "D"],
    [lambda x: x < 60, "C"],
    [lambda x: x < 85, "B"],
    [T, "A"],
  ])
  assert f(0) == "D"
  assert f(30) == "C"
  assert f(40) == "C"
  assert f(80) == "B"
  assert f(99) == "A"

  g = cond([
    [lambda x: x < 30, lambda x: str(x) + ": D"],
    [lambda x: x < 60, lambda x: str(x) + ": C"],
    [lambda x: x < 85, lambda x: str(x) + ": B"],
    [T, lambda x: str(x) + ": A"],
  ])
  assert g(0) == "0: D"
  assert g(30) == "30: C"
  assert g(40) == "40: C"
  assert g(80) == "80: B"
  assert g(99) == "99: A"

def test_defaultto():
  assert defaultto(100)(42) == 42
  assert defaultto(42)(None) == 42
