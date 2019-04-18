import functools
def curry(f, wargs=[], wkwargs={}):
  @functools.wraps(f)
  def wrapper(*nargs, **nkwargs):
    args = wargs + list(nargs)
    kwargs = {**nkwargs, **nkwargs}
    arity = f.__code__.co_argcount
    if len(args) + len(kwargs) >= arity:
      return f(*args, **kwargs)
    return curry(f, args)
  return wrapper