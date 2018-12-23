
__all__ = ("inspect",)

def inspect(x):
  if hasattr(x, "inspect"):
    return x.inspect()
  else:
    return x