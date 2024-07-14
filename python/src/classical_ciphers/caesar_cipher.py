class CaesarCipher:
    def __init__(self, key):
        self.key = int(key)
        
    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                shifted = ord(char) + self.key
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    ciphertext += chr(shifted)
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    ciphertext += chr(shifted)
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = ord(char) - self.key
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                    plaintext += chr(shifted)
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                    plaintext += chr(shifted)
            else:
                plaintext += char
        return plaintext
