from . import curry, identity, inspect
#from .util import inspect

__all__ = ("Either", "left", "either")

@curry
def either(f, g, e):
  if isinstance(e, Left):
    return f(e._value)

  if isinstance(e, Right):
    return g(e._value)

class Either(object):
  def __init__(self, v):
    self._value = v

  @staticmethod
  def of(v):
    return Right(v)

left = lambda v: Left(v)
class Left(Either):
  @property
  def isleft(self):
    return True

  @property
  def isright(self):
    return False

  def fmap(self, f):
    return self

  def inspect(self) -> str:
    return f"Left({inspect(self._value)})"

  def join(self):
    return self

  def chain(self, f):
    return self

  def sequence(self, of):
    return of(self)

  def traverse(self, of, f):
    return of(self)

class Right(Either):
  @property
  def isleft(self) -> bool:
    return False

  @property
  def isright(self) -> bool:
    return True

  def fmap(self, f):
    return Either.of(f(self._value))

  def inspect(self) -> str:
    return f"Right({inspect(self._value)})"

  def join(self):
    return self._value

  def chain(self, f):
    return f(self._value)

  def sequence(self, of):
    return self.traverse(of, identity)

  def traverse(self, of, f):
    return f(self._value).fmap(Either.of)