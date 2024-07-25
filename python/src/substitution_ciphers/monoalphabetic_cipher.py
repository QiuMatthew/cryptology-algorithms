class MonoalphabeticCipher:
    def __init__(self, key):
        if len(key) != 26:
            raise ValueError("Key string must be exactly 26 characters long")
        self.forward = {chr(ord('a') + i): key[i].lower() for i in range(26)}
        self.forward.update({chr(ord('A') + i): key[i].upper() for i in range(26)})
        self.backward = {key[i].lower(): chr(ord('a') + i) for i in range(26)}
        self.backward.update({key[i].upper(): chr(ord('A') + i) for i in range(26)})
    
    def encrypt(self, plaintext):
        ciphertext = ""
        for p in plaintext:
            if p.isalpha():
                c = self.forward[p]
            else:
                c = p
            ciphertext += c
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for c in ciphertext:
            if c.isalpha():
                p = self.backward[c]
            else:
                p = c
            plaintext += p
        return plaintext

