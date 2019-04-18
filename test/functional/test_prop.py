from ftool.functional.prop import prop

def test_prop():
  class A():
    a = 42
    b = "hello"
  a = A()
  d = dict(a = 42, b = "hello")
  assert prop("a", a) == 42
  assert prop("c", a) is None
  assert prop("a", d) == 42
  assert prop("c", d) is None