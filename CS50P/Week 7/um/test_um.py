from um import count

def test_contains_um():
    assert count('hey um how are you') == 1
    assert count('hello ,um world') == 1
    assert count('!um.') == 1

def test_no_um():
    assert count('yummy') == 0
    assert count('humpty dumpty sat on a wall') == 0
    assert count('hello how are you') == 0


def test_caps():
    assert count('hey Um how are you?') == 1
    assert count('No Um, thats not Um...') == 2
    assert count('Um') == 1
    assert count('UM') == 1

def test_spaces():
    assert count('um') == 1
    assert count('um, mum?') == 1
