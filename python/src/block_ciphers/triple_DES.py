from .DES import DESCipher
from ..proto.block_cipher import BlockCipher

class TripleDESCipher(BlockCipher):
    def __init__(self, key1: str, key2: str, key3: str) -> None:
        self.des1 = DESCipher(key1)
        self.des2 = DESCipher(key2)
        self.des3 = DESCipher(key3)

    def encrypt(self, plaintext: str) -> str:
        bin_plaintext = self.des1._str_to_bin(plaintext)
        encrypted = self.des1.bin_to_bin_encrypt(bin_plaintext)
        decrypted = self.des2.bin_to_bin_decrypt(encrypted)
        bin_ciphertext = self.des3.bin_to_bin_encrypt(decrypted)
        hex_ciphertext = self.des3._bin_to_hex(bin_ciphertext)
        return hex_ciphertext
        
    def decrypt(self, ciphertext: str) -> str:
        # NOTE: ciphertext is hexadecimal while plaintext is readable string
        bin_ciphertext = self.des3._hex_to_bin(ciphertext)
        decrypted = self.des3.bin_to_bin_decrypt(bin_ciphertext)
        encrypted = self.des2.bin_to_bin_encrypt(decrypted)
        bin_plaintext = self.des1.bin_to_bin_decrypt(encrypted)
        plaintext = self.des1._bin_to_str(bin_plaintext)
        return plaintext

if __name__ == "__main__":
    key1 = "testkey1"
    key2 = "testkey2"
    key3 = "testkey3"
    cipher = TripleDESCipher(key1, key2, key3)
    plaintext = "plaintxt"
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
