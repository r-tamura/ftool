from ftool import IO

def test_run():
  greeting = lambda: "hello, world"
  assert IO(greeting).run() == "hello, world"

def test_of():
  assert IO.of("hello, world").run() == "hello, world"

def test_fmap():
  greeting = lambda: "hello, world"
  toupper = lambda s: s.upper()
  assert IO(greeting).fmap(toupper).run() == "HELLO, WORLD"

def test_chain():
  id = IO.of("1000")
  user = lambda id: IO.of({ "id": id })
  assert id.chain(user).run() == { "id": "1000" }

def test_join():
  id = IO.of("1000")
  user = lambda id: IO.of({ "id": id })
  assert id.fmap(user).join().run() == { "id": "1000" }

