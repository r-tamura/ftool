from ftool import Container, Either

def test_of():
  assert Container.of(42)._value == 42

def test_fmap():
  assert Container.of(21).fmap(lambda x: x * 2)._value == 42

def test_ap():
  f = lambda x: lambda y: x + y
  c1 = Container.of(3)
  c2 = Container.of(39)
  assert Container.of(f).ap(c1).ap(c2)._value == 42

def test_join():
  assert Container.of(42).join() == 42

def test_chain():
  assert Container.of(21).fmap(lambda x: x * 2).join() == 42

def test_sequence():
  assert Container.of(Either.of(42)).sequence(None).join().join() == 42

def test_traverse():
  assert Container.of(42).traverse(None, Either.of).join().join() == 42