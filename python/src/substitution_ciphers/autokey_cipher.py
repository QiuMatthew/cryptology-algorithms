from ..proto.substitution_cipher import SubstitutionCipher

class AutokeyCipher(SubstitutionCipher):
    def __init__(self, keyword):
        self.keyword = self.preprocess_text(keyword).upper()
        self.keylen = len(self.keyword)

    def encrypt(self, plaintext):
        plaintext = self.preprocess_text(plaintext).lower()
        ciphertext = ""
        for i, char in enumerate(plaintext):
            if i < len(self.keyword):
                shifted = ord(char) + ord(self.keyword[i]) - ord("A")
            else:
                shifted = ord(char) + ord(plaintext[i - len(self.keyword)]) - ord("a")
            if shifted > ord("z"):
                shifted -= 26
            ciphertext += chr(shifted)
        return ciphertext.upper()

    def decrypt(self, ciphertext):
        ciphertext = self.preprocess_text(ciphertext).upper()
        plaintext = ""
        for i, char in enumerate(ciphertext):
            if i < len(self.keyword):
                shifted = ord(char) - ord(self.keyword[i]) + ord('A')
            else:
                shifted = ord(char) - ord(plaintext[i - len(self.keyword)]) + ord('A')
            if shifted < ord('A'):
                shifted += 26
            plaintext += chr(shifted)
        return plaintext.lower()

if __name__ == "__main__":
    keyword = "deceptive"
    cipher = AutokeyCipher(keyword)
    
    plaintext = "wearediscoveredsaveyourself"
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")

