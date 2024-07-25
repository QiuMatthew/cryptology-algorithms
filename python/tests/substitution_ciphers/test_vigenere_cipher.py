import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from substitution_ciphers.vigenere_cipher import VigenereCipher

def test_vigenere_cipher():
    keyword = "deceptive"
    cipher = VigenereCipher(keyword)
    plaintext = "we are discovered save yourself"
    ciphertext = cipher.encrypt(plaintext)
    assert cipher.decrypt(ciphertext) == cipher.preprocess_text(plaintext)

if __name__ == "__main__":
    pytest.main()
