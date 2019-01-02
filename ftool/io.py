from . import compose, inspect

__all__ = ("IO",)

class IO():
  """
  > IO delays the impure action by capturing it in a function wrapper.
  > As such, we think of IO as "containing the return value of the wrapped
  > action" and not the wrapper itself.
  https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch08.html#old-mcdonald-had-effects
  """
  def __init__(self, io):
    self._io = io

  @staticmethod
  def of(v):
    return IO(lambda: v)

  # Functor IO
  def fmap(self, f):
    return IO(compose(f, self._io))

  # Monad IO
  def join(self):
    return IO.of(self.run().run())

  def chain(self, f):
    return self.fmap(f).join()

  def inspect(self):
    return f"IO({inspect(self._io)})"

  def run(self):
    return self._io()