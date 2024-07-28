import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.substitution_ciphers.caesar_cipher import CaesarCipher

def test_encrypt():
    cipher = CaesarCipher(3)
    assert cipher.encrypt("hello") == "KHOOR"
    assert cipher.encrypt("world") == "ZRUOG"
    assert cipher.encrypt("HELLO") == "KHOOR"
    assert cipher.encrypt("WORLD") == "ZRUOG"
    assert cipher.encrypt("hello world") == "KHOORZRUOG"

def test_decrypt():
    cipher = CaesarCipher(3)
    assert cipher.decrypt("khoor") == "hello"
    assert cipher.decrypt("zruog") == "world"
    assert cipher.decrypt("KHOOR") == "hello"
    assert cipher.decrypt("ZRUOG") == "world"
    assert cipher.decrypt("khoor zruog") == "helloworld"
    
def test_non_alpha_characters():
    cipher = CaesarCipher(3)
    assert cipher.encrypt("hello, I'm 123") == "KHOORLP"
    assert cipher.decrypt("KHOOR, L'P 123") == "helloim"

if __name__ == "__main__":
    pytest.main()
