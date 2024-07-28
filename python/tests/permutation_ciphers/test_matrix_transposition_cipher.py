import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.permutation_ciphers.matrix_transposition_cipher import MatrixTranspositionCipher

def test_matrix_transposition_cipher():
    cipher = MatrixTranspositionCipher()
    plaintext = "meetmeafterthetogaparty"
    ciphertext = cipher.encrypt(plaintext)
    assert(cipher.decrypt(ciphertext) == cipher.preprocess_text(plaintext))

if __name__ == "__main__":
    pytest.main()

