import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.block_ciphers.DES import DESCipher

def test_DES():
    key = "yjsnpy64"
    cipher = DESCipher(key)
    plaintext = "64bblock"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == plaintext

if __name__ == "__main__":
    pytest.main()
