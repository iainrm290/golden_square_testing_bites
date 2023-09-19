from lib.check_codeword import *

def test_with_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_with_house():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_for_wrong():
    result = check_codeword("bacon")
    assert result == "WRONG!"