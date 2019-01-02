from ftool import Maybe

def test_of():
  assert Maybe.of(42)._value == 42

def test_fmap():
  double = lambda x: x * 2
  assert Maybe.of(21).fmap(double)._value == 42
  assert Maybe.from_nullable(None).fmap(double)._value  == None

def test_inspect():
  assert Maybe.of("hello, world").inspect() == "Just(hello, world)"
  assert Maybe.from_nullable(None).inspect() == "Nothing()"

def test_isjust_isnothing():
  j = Maybe.from_nullable(42)
  n = Maybe.from_nullable(None)

  assert j.isjust
  assert not j.isnothing
  assert not n.isjust
  assert n.isnothing

def test_ap():
  add = lambda x: lambda y: x + y
  assert Maybe.from_nullable(add).ap(Maybe.of(3)).ap(Maybe.of(39))._value == 42
  assert Maybe.from_nullable(None).ap(Maybe.of(3)).ap(Maybe.of(39))._value == None

def test_join():
  assert Maybe.from_nullable(42).join() == 42
  assert Maybe.from_nullable(None).join() == None

def test_chain():
  add1 = lambda x: x + 1
  assert Maybe.from_nullable(41).chain(add1) == 42
  assert Maybe.from_nullable(None).chain(add1) == None