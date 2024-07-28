import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.substitution_ciphers.hill_cipher import HillCipher

def test_hill_cipher():
    keyMatrix = [[7, 8], [11, 11]]
    cipher = HillCipher(keyMatrix)
    plaintext = "Hello World"
    ciphertext = cipher.encrypt(plaintext)
    assert cipher.decrypt(ciphertext)[:len(plaintext)] == cipher.preprocess_plaintext(plaintext)

if __name__ == "__main__":
    pytest.main()
