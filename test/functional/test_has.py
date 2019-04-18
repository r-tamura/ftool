from ftool.functional.has import has

def test_has_given_dict():
  assert has("a", dict(a = 42, b = "hello"))
  assert not has("c", dict(a = 42, b = "hello"))

def test_has_given_obj():
  class A():
    a = 42
    b = "hello"
  a = A()
  assert has("a", a)
  assert not has("d", a)