import pytest
from lib.present import *

def test_present_contents():
    present = Present()
    result = present.contents
    assert result == None

def test_present_wrap():
    present = Present()
    present.contents = "toys"
    with pytest.raises(Exception) as e:
        present.wrap("socks")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_present_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."