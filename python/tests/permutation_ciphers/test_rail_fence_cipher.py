import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.permutation_ciphers.rail_fence_cipher import RailFenceCipher

def test_rail_fence_cipher():
    row_count = 2
    cipher = RailFenceCipher(row_count)
    plaintext = "meetmeafterthetogaparty"
    ciphertext = cipher.encrypt(plaintext)
    assert(cipher.decrypt(ciphertext) == plaintext)

    row_count = 5
    cipher = RailFenceCipher(row_count)
    plaintext = "wearediscoveredsaveyourself"
    ciphertext = cipher.encrypt(plaintext)
    assert(cipher.decrypt(ciphertext) == plaintext)

if __name__ == "__main__":
    pytest.main()
