import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.block_ciphers.AES import AESCipher

def test_DES():
    key = "thisisakey123456"
    cipher = AESCipher(key)
    plaintext = "thisisplaintext1"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == plaintext

def test_encrypt():
    key = "thisisakey123456"
    cipher = AESCipher(key)
    assert cipher.encrypt("thisisplaintext1") == "fa0fb03bb5258ae2ee3f274735b57651"

def test_decrypt():
    key = "thisisakey123456"
    cipher = AESCipher(key)
    assert cipher.decrypt("fa0fb03bb5258ae2ee3f274735b57651") == "thisisplaintext1"

def test_galois_field_mul():
    key = "thisisakey123456"
    cipher = AESCipher(key)
    assert cipher.galois_field_mul(0x02, 0xd4) == 0xb3
    assert cipher.galois_field_mul(0x03, 0xbf) == 0xda
    assert cipher.galois_field_mul(0x01, 0x5d) == 0x5d
    assert cipher.galois_field_mul(0x01, 0x30) == 0x30

def test_mix_columns():
    key = "thisisakey123456"
    cipher = AESCipher(key)
    input_state = [
        [ 0xd4, 0xe0, 0xb8, 0x1e ],
        [ 0xbf, 0xb4, 0x41, 0x27 ],
        [ 0x5d, 0x52, 0x11, 0x98 ],
        [ 0x30, 0xae, 0xf1, 0xe5 ],
    ]
    output_state = [
        [ 0x04, 0xe0, 0x48, 0x28 ],
        [ 0x66, 0xcb, 0xf8, 0x06 ],
        [ 0x81, 0x19, 0xd3, 0x26 ],
        [ 0xe5, 0x9a, 0x7a, 0x4c ],
    ]
    assert cipher.mix_columns(input_state) == output_state

if __name__ == "__main__":
    pytest.main()
