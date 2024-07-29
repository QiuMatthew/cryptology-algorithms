import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.block_ciphers.triple_DES import TripleDESCipher

def test_triple_DES():
    key1 = "testkey1"
    key2 = "testkey2"
    key3 = "testkey3"
    cipher = TripleDESCipher(key1, key2, key3)
    plaintext = "plaintxt"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == plaintext

if __name__ == "__main__":
    pytest.main()
