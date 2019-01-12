from .core import identity
__all__ = ("Container", )

class Container():
  def __init__(self, v):
    self._value = v

  @staticmethod
  def of(v):
    return Container(v)

  # Container Functor
  def fmap(self, f):
    return Container(f(self._value))

  # Container Applicative
  def ap(self, v):
    return v.fmap(self._value)

  # Container Monad
  def join(self):
    return self._value

  def chain(self, f):
    return self.fmap(f).join()

  def sequence(self, of):
    return self.traverse(of, identity)

  def traverse(self, of, f):
    return f(self._value).fmap(Container.of)