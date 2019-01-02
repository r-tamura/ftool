from ftool.util import log

def test_log(capsys):
  assert log("hello, world") == "hello, world"

  captured = capsys.readouterr()
  assert captured.out == "hello, world\n"