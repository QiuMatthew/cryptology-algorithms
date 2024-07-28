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
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    p = ord(char) - ord('a')
                    c = (p * self.keyA + self.keyB) % 26
                    ciphertext += chr(ord('a') + c)
                elif char.isupper():
                    p = ord(char) - ord('A')
                    c = (p * self.keyA + self.keyB) % 26
                    ciphertext += chr(ord('A') + c)
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                # calculate modular multiplication inverse of a
                a_inv = pow(self.keyA, -1, 26)
                if char.islower():
                    c = ord(char) - ord('a')
                    p = ((c - self.keyB) * a_inv) % 26
                    plaintext += chr(ord('a') + p)
                elif char.isupper():
                    c = ord(char) - ord('A')
                    p = ((c - self.keyB) * a_inv) % 26
                    plaintext += chr(ord('A') + p)
            else:
                plaintext += char
        return plaintext
