from bank import value

def test_startswith_h():
    assert value('hi, dave') == 20


def test_hello():
    assert value('hello') == 0


def test_other():
    assert value("What's up?") == 100


def test_numbers():
    assert value('123') == 100


def test_symbols():
    assert value('+ hi') == 100

def test_capital():
    assert value('HELLO') == 0