import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.permutation_ciphers.columnar_transposition_cipher import ColumnarTranspositionCipher

def test_columnar_transposition_cipher():
    keyword = "dcabefg"
    cipher = ColumnarTranspositionCipher(keyword)
    plaintext = "attackpostponeduntiltwoam"
    ciphertext = cipher.encrypt(plaintext)
    assert(cipher.decrypt(ciphertext) == cipher.preprocess_plaintext(plaintext))

if __name__ == "__main__":
    pytest.main()
