import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from substitution_ciphers.playfair_cipher import PlayfairCipher

def test_playfair_cipher():
    keyword = "MONARCHY"
    cipher = PlayfairCipher(keyword)
    plaintext = "HELLO WORLD"
    ciphertext = cipher.encrypt(plaintext)
    assert cipher.decrypt(ciphertext) == cipher.preprocess_text(plaintext)

if __name__ == "__main__":
    pytest.main()
