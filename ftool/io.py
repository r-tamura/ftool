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
    self.unsafe_perform_io = io

  @classmethod
  def of(cls, v):
    return cls(lambda: v)

  def fmap(self, f):
    return IO(compose(f, self.unsafe_perform_io))

  def inspect(self):
    return f"IO({inspect(self.unsafe_perform_io)})"