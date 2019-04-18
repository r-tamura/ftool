from .curry import curry
from .prop import prop
@curry
def has(key: str, o):
  return prop(key, o) is not None
