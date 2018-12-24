from . import tap

__all__ = ("inspect", "log")

def inspect(x):
  if hasattr(x, "inspect"):
    return x.inspect()
  else:
    return x

@tap
def log(x):
  print(x)