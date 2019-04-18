from .curry import curry
@curry
def prop(name, o):
  """
  >>> get_name = prop("name")
  >>> a = {"prop1": "value1", "name": "John"}
  >>> get_name(a)
  'John'
  """
  if isinstance(o, dict):
    return o.get(name, None)
  return getattr(o, name, None)