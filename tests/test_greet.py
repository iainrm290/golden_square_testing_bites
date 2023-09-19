from lib.greet import *

def test_greet_returns_name():
    result = greet("Iain")
    assert result == "Hello, Iain!"