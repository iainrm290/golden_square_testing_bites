from lib.string_builder import *

def test_string_builder_adds_str():
    string_builder = StringBuilder()
    string_builder.add("yes")
    result = string_builder.output()
    assert result == "yes"

def test_string_builder_gets_length():
    string_builder = StringBuilder()
    string_builder.add("yeesss")
    result = string_builder.size()
    assert result == 6
