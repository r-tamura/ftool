import math
import random
import ftool as F

# class Container(object):
#   def __init__(self, v):
#     self._value = v

#   @classmethod
#   def of(cls, v):
#     return cls(v)

#   def map(self, f):
#     return self.__class__.of(f(self._value))

if __name__ == "__main__":
  # Maybe
  print(F.inspect(F.Maybe.of(3)))
  print(F.inspect(F.Maybe.of(None)))
  print(F.inspect(F.Maybe.of("John").fmap(lambda s: "Hello, " + s)))
  print(F.inspect(F.Maybe.of("John").fmap(lambda s: None)))

  # Either
  print(F.inspect(F.Either.of("rain").fmap(lambda s: f"b{s}")))

  def random_error():
    return F.Either.of("ok") if random.random() > 0.5 else F.left("fail")
  F.compose(
    print,
    F.either(F.identity, F.identity),
    F.map(lambda s: f"{s}!!"),
    random_error,
  )()

  # IO
  r = lambda: F.IO.of(random.random())


  print(F.compose(
    F.map(lambda s: f"{s} %"),
    F.map(lambda n: str(n)),
    F.map(lambda x: math.floor(x * 100)),
    r,
  )().unsafe_perform_io())




