import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.stream_ciphers.rc4 import RC4Cipher

def test_RC4():
    key = "yjsnpy"
    cipher = RC4Cipher(key.encode())
    plaintext = "datastreamwithrandomlength"
    encrypted = cipher.encrypt(plaintext.encode())
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == plaintext.encode()

if __name__ == "__main__":
    pytest.main()
