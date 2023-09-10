import fuel
import pytest

def test_convert_not_int():
    with pytest.raises(ValueError):
        fuel.convert('cat')

    with pytest.raises(ValueError):
        fuel.convert('cat / dog')

def test_convert_y_is_zero():
    with pytest.raises(ZeroDivisionError):
        fuel.convert('1 / 0')

def test_convert_x_greater():
    with pytest.raises(ValueError):
        fuel.convert('3 / 2')
def test_convert_int():
    assert fuel.convert('1 / 2') == 50
    
def test_gauge_E():
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(0) == 'E'

def test_gauge_F():
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(100) == 'F'

def test_gauge_percentage():
    assert fuel.gauge(56) == '56%'