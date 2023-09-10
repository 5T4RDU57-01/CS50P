from seasons import validation
from seasons import get_minutes
from seasons import mins_to_words

def test_validation():
    assert validation('2007-08-23') == True
    assert validation('January 27, 2008') == False
    assert validation('08-2007-23') == False
    assert validation('2002-31-12') == False
    assert validation('2003-00-01') == False
    assert validation('2003-6-4') == False

def test_get_minutes():
    assert get_minutes('2022-09-01') == 525600

def test_mins_to_words():
    assert mins_to_words(525600) == 'Five hundred twenty-five thousand, six hundred'