from ..proto.substitution_cipher import SubstitutionCipher

class MonoalphabeticCipher(SubstitutionCipher):
    """
    Key: A permutation of alphabet, use it as a mapping f: alphabet -> alphabet
    Encrypt: c = f(p)
    Decrypt: p = f^{-1}(c)
    """
    def __init__(self, key):
        if len(key) != 26:
            raise ValueError("Key string must be exactly 26 characters long")
        self.forward = {chr(ord('a') + i): key[i].upper() for i in range(26)}
        self.backward = {key[i].upper(): chr(ord('a') + i) for i in range(26)}
    
    def encrypt(self, plaintext):
        plaintext = self.preprocess_plaintext(plaintext)
        ciphertext = ""
        for char in plaintext:
            ciphertext += self.forward[char]
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self.preprocess_ciphertext(ciphertext)
        plaintext = ""
        for char in ciphertext:
            plaintext += self.backward[char]
        return plaintext

