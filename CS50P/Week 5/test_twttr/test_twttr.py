from twttr import shorten

def test_has_vovels():
    assert shorten('twitter') == 'twttr'
    assert shorten('hello') == 'hll'

def test_has_no_vovels():
    assert shorten('lynch') == 'lynch'
    assert shorten('gym') == 'gym'

def test_has_capital():
    assert shorten('INSIGNIA') == 'NSGN'
    assert shorten('ELONGATE') == 'LNGT'

def test_has_punctuation():
    assert shorten('hello, world') == 'hll, wrld'

def test_has_numbers():
    assert shorten('hello 123') == 'hll 123'