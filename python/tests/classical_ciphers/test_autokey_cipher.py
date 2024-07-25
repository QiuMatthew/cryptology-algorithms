import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from classical_ciphers.autokey_cipher import AutokeyCipher

def test_autokey_cipher():
    keyword = "deceptive"
    cipher = AutokeyCipher(keyword)
    plaintext = "wearediscoveredsaveyourself"
    ciphertext = cipher.encrypt(plaintext)
    assert(cipher.decrypt(ciphertext) == cipher.preprocess_text(plaintext))

if __name__ == "__main__":
    pytest.main()
