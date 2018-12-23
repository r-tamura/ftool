from .util import inspect

__all__ = ("Maybe",)

class Maybe(object):
  def __init__(self, v):
    self._value = v

  @classmethod
  def of(cls, v):
    return cls(v)

  @property
  def isnothing(self):
    return self._value is None

  def map(self, f):
    return self if self.isnothing else self.__class__.of(f(self._value))

  def inspect(self):
    return "Nothing" if self.isnothing else f"Just({inspect(self._value)})"