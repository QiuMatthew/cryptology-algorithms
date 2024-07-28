from ..proto.substitution_cipher import SubstitutionCipher

class AffineCipher(SubstitutionCipher):
    '''
    Key: a, b
    Encrypt: c = ap + b mod 26
    Decrypt: p = (c - b) / a mod 26
    '''
    def __init__(self, a, b):
        self.keyA = a
        self.keyB = b

    def encrypt(self, plaintext):
        plaintext = self.preprocess_plaintext(plaintext)
        ciphertext = ""
        for char in plaintext:
            p = ord(char) - ord('a')
            c = (p * self.keyA + self.keyB) % 26
            ciphertext += chr(ord('a') + c)
        return ciphertext.upper()

    def decrypt(self, ciphertext):
        ciphertext = self.preprocess_ciphertext(ciphertext)
        plaintext = ""
        for char in ciphertext:
            # calculate modular multiplication inverse of a
            a_inv = pow(self.keyA, -1, 26)
            c = ord(char) - ord('A')
            p = ((c - self.keyB) * a_inv) % 26
            plaintext += chr(ord('A') + p)
        return plaintext.lower()
