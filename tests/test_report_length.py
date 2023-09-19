from lib.report_length import *

def test_report_length():
    result = report_length("123456789")
    assert result == "This string was 9 characters long."

def test_report_with_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."