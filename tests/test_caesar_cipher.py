from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    assert encrypt('abc', 1) == 'bcd'
    assert encrypt('abc', 10) == 'klm'
    assert encrypt('abc', 26) == 'abc'
    assert encrypt('BASMA', 30) == 'FEWQE'

def test_decrypt():
    assert decrypt('bcd', 1) == 'abc'
    assert decrypt('klm', 10) == 'abc'
    assert decrypt('abc', 26) == 'abc'
    assert decrypt('FEWQE', 30) == 'BASMA'