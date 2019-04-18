from ftool import curry

def test_curry():
  add = curry(lambda x, y: x + y)
  mul = curry(lambda x, y: x * y)
  add3 = add(3)
  mul6 = mul(6)
  assert add3(39) == 42
  assert mul6(7) == 42