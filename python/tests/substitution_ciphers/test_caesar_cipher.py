import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.substitution_ciphers.caesar_cipher import CaesarCipher

def test_encrypt():
    cipher = CaesarCipher(3)
    assert cipher.encrypt("hello") == "khoor"
    assert cipher.encrypt("world") == "zruog"
    assert cipher.encrypt("HELLO") == "KHOOR"
    assert cipher.encrypt("WORLD") == "ZRUOG"
    assert cipher.encrypt("hello world") == "khoor zruog"

def test_decrypt():
    cipher = CaesarCipher(3)
    assert cipher.decrypt("khoor") == "hello"
    assert cipher.decrypt("zruog") == "world"
    assert cipher.decrypt("KHOOR") == "HELLO"
    assert cipher.decrypt("ZRUOG") == "WORLD"
    assert cipher.decrypt("khoor zruog") == "hello world"
    
def test_non_alpha_characters():
    cipher = CaesarCipher(3)
    assert cipher.encrypt("hello123") == "khoor123"
    assert cipher.decrypt("khoor123") == "hello123"

if __name__ == "__main__":
    pytest.main()
