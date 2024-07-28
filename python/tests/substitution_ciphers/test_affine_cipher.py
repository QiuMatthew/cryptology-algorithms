import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.substitution_ciphers.affine_cipher import AffineCipher

def test_encrypt():
    cipher = AffineCipher(3, 2)
    assert cipher.encrypt("crypto") == "IBWVHS"
    assert cipher.encrypt("Hello World") == "XOJJSQSBJL"
    assert cipher.encrypt("yjsnpy114514") == "WDEPVW"

def test_decrypt():
    cipher = AffineCipher(3, 2)
    assert cipher.decrypt("ibwvhs") == "crypto"
    assert cipher.decrypt("Xojjs Qsbjl") == "helloworld"
    assert cipher.decrypt("wdepvw114514") == "yjsnpy"

if __name__ == "__main__":
    pytest.main()
