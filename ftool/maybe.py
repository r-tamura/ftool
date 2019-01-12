from .util import inspect

__all__ = ("Maybe",)

class Maybe():
  def __init__(self, v):
    pass

  @staticmethod
  def of(v):
    return Just.of(v)

  @staticmethod
  def from_nullable(v):
    return Just.of(v) if v is not None else Nothing.of(v)

  @property
  def isnothing(self):
    pass

  @property
  def isjust(self):
    pass

  def fmap(self, f):
    return None

  def inspect(self):
    return ""

class Just(Maybe):
  def __init__(self, v):
    self._value = v

  @staticmethod
  def of(v):
    return Just(v)

  @property
  def isnothing(self):
    return False

  @property
  def isjust(self):
    return True

  # Functor
  def fmap(self, f):
    return Maybe.of(f(self._value))

  # Applicative
  def ap(self, f):
    return f.fmap(self._value)

  # Monad
  def chain(self, f):
    return f(self._value)

  def join(self):
    return self._value

  def inspect(self):
    return f"Just({inspect(self._value)})"

class Nothing(Maybe):
  def __init__(self, _):
    self._value = None

  @staticmethod
  def of(v):
    return Nothing(v)

  @property
  def isnothing(self):
    return True

  @property
  def isjust(self):
    return False

  # Functor
  def fmap(self, f):
    return self

  # Applicative
  def ap(self, f):
    return self

  # Monad
  def chain(self, f):
    return self.join()

  def join(self):
    return None

  def inspect(self):
    return "Nothing()"
