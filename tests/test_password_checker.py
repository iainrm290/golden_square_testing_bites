import pytest
from lib.password_checker import *

def test_password_checker():
    password_checker = PasswordChecker()
    result = password_checker.check("12345678")
    assert result == True

def test_password_checker_too_short():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("123456")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."