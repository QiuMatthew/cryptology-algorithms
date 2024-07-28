import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.substitution_ciphers.monoalphabetic_cipher import MonoalphabeticCipher

def test_encryption():
    key = "DKVQFIBJWPESCXHTMYAUOLRGZN"
    cipher = MonoalphabeticCipher(key)
    plaintext = "if we wish to replace letters"
    assert cipher.encrypt(plaintext) == "WIRFRWAJUHYFTSDVFSFUUFYA"

def test_decryption():
    key = "DKVQFIBJWPESCXHTMYAUOLRGZN"
    cipher = MonoalphabeticCipher(key)
    ciphertext = "WIRFRWAJUHYFTSDVFSFUUFYA"
    assert cipher.decrypt(ciphertext) == "ifwewishtoreplaceletters"

if __name__ == "__main__":
    pytest.main()

