from plates import is_valid

def test_startswith_letters():
    assert is_valid('SAS123') == True
    assert is_valid('123SAS') == False
    assert is_valid('SA1234') == True
    assert is_valid('S12345') == False

def test_range():
    assert is_valid('A') == False
    assert is_valid('ABC1234') == False

def test_num_in_middle():
    assert is_valid('AB123C') == False
    assert is_valid('A12BC') == False


def test_startswith_zero():
    assert is_valid('ABC012') == False
    assert is_valid('ABC123') == True

def test_no_symbols():
    assert is_valid('?ABC12') == False
    assert is_valid('@BCD1') == False
    assert is_valid('ABC!23') == False
