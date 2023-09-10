from working import convert
import pytest


def test_syntax():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:30 AM to 5:30 PM') == '09:30 to 17:30'
    assert convert('1 PM to 4 PM') == '13:00 to 16:00'


def test_range():
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        convert('13 AM to 14 PM')
    with pytest.raises(ValueError):
        convert('10:72 AM to 3:98 PM')


