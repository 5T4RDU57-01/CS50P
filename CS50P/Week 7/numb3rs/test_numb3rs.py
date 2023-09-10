from numb3rs import validate

def test_actual_ip():
    assert validate('192.168.1.1') == True
    assert validate('1.1.1.1') == True
    assert validate('1.1.1') == False



def test_strings():
    assert validate('cat') == False
    assert validate('dogs are batter!') == False

def test_range():
    assert validate('0.0.0.0') == True
    assert validate('300.1.3.4') == False
    assert validate('1.300.454.1222') == False
    assert validate('192.188.300.40') == False