from ..proto.substitution_cipher import SubstitutionCipher

class CaesarCipher(SubstitutionCipher):
    '''
    Key: key
    Encrypt: c = p + key mod 26
    Decrypt: p = c - key mod 26
    '''
    def __init__(self, key):
        self.key = int(key)
        
    def encrypt(self, plaintext) -> str:
        plaintext = self.preprocess_text(plaintext).lower()
        ciphertext = ""
        for char in plaintext:
            shifted = ord(char) + self.key
            if shifted > ord('z'):
                shifted -= 26
            ciphertext += chr(shifted)
        return ciphertext.upper()

    def decrypt(self, ciphertext) -> str:
        ciphertext = self.preprocess_text(ciphertext).upper()
        plaintext = ""
        for char in ciphertext:
            shifted = ord(char) - self.key
            if shifted < ord('A'):
                shifted += 26
            plaintext += chr(shifted)
        return plaintext.lower()

