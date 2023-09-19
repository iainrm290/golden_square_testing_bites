from lib.add_five import *

def test_add_five_returns_eight_for_three():
    result = add_five(5)
    assert result == 8