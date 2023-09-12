from project import ui_validation , cli_validation , encrypt , decrypt , key_validation

def test_ui_validation():
    assert ui_validation(-1) == False
    assert ui_validation(5) == False
    assert ui_validation('three') == False


def test_cli_validation():
    assert cli_validation('-e' , 5 , 'key.key') == False
    assert cli_validation('-e' , 4 , 'key.key') == True
    assert cli_validation('-e' , 3 , 'key.key') == False
    assert cli_validation('-d' , 3 , 'key.key') == False
    assert cli_validation('-g' , 3 , 'key.key') == True
    assert cli_validation('-h' , 2) == True
    assert cli_validation('-h' , 3) == False


def test_encrypt():
    assert encrypt('non-existant-file.txt' , 'non-existant-key.key') == False
    assert encrypt(r'key_file\existant-file.txt' , 'non-existant-key.key') == False
    assert encrypt('non-existant-file.txt' , r'key_file\existant-key.key') == False

def test_decrypt():
    assert decrypt('non-existant-file.txt' , 'non-existant-key.key') == False
    assert decrypt(r'key_file\existant-file.txt' , 'non-existant-key.key') == False
    assert decrypt('non-existant-file.txt' , r'key_file\existant-key.key') == False

def test_key_vaidation():
    assert key_validation(123) == False
    assert key_validation('test.txt') == False
    assert key_validation('test.key') == True