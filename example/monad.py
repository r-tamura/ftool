import random
import ftool as F

def map(f):
  return lambda x: x.map(f)

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
  print(F.inspect(F.Maybe.of("John").map(lambda s: "Hello, " + s)))
  print(F.inspect(F.Maybe.of("John").map(lambda s: None)))

  # Either
  print(F.inspect(F.Either.of("rain").map(lambda s: f"b{s}")))

  def randome_error():
    return F.Either.of("ok") if random.random() > 0.5 else F.left("fail")
  F.compose(
    print,
    F.either(F.identity, F.identity),
    map(lambda s: f"{s}!!"),
    randome_error,
  )()

  # IO


