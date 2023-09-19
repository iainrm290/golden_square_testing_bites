from lib.gratitudes import *

def test_gratitudes_appends_to_list():
    gratitudes = Gratitudes()
    gratitudes.add("Rainy days")
    result = gratitudes.gratitudes
    assert result == ["Rainy days"]

def test_gratitudes_format():
    gratitudes = Gratitudes()
    gratitudes.add("Rainy days")
    result = gratitudes.format()
    assert result == "Be grateful for: Rainy days"