import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from classical_ciphers.caesar_cipher import encrypt, decrypt

def test_encrypt():
    assert encrypt("hello", 3) == "khoor"
    assert encrypt("world", 5) == "btwqi"
    assert encrypt("HELLO", 3) == "KHOOR"
    assert encrypt("WORLD", 5) == "BTWQI"
    assert encrypt("hello world", 3) == "khoor zruog"

def test_decrypt():
    assert decrypt("khoor", 3) == "hello"
    assert decrypt("btwqi", 5) == "world"
    assert decrypt("KHOOR", 3) == "HELLO"
    assert decrypt("BTWQI", 5) == "WORLD"
    assert decrypt("khoor zruog", 3) == "hello world"
    
def test_non_alpha_characters():
    assert encrypt("hello123", 3) == "khoor123"
    assert decrypt("khoor123", 3) == "hello123"

if __name__ == "__main__":
    pytest.main()
