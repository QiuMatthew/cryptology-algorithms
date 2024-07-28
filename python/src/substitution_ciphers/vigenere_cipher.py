from ..proto.substitution_cipher import SubstitutionCipher

class VigenereCipher(SubstitutionCipher):
    """
    Key: key = k_0 k_1 k_2 ... k_{n-1}
    Encrypt: c_i = p_i + k_i mod 26
    Decrypt: p_i = c_i - k_i mod 26
    """
    def __init__(self, keyword) -> None:
        self.keyword = keyword.upper()
        self.keylen = len(self.keyword)

    def encrypt(self, plaintext):
        plaintext = self.preprocess_plaintext(plaintext)
        ciphertext = ""
        for i, char in enumerate(plaintext):
            shifted = ord(char) + ord(self.keyword[i % self.keylen]) - ord('A')
            if shifted > ord('z'):
                shifted -= 26
            ciphertext += chr(shifted)
        return ciphertext.upper()

    def decrypt(self, ciphertext):
        ciphertext = self.preprocess_ciphertext(ciphertext)
        plaintext = ""
        for i, char in enumerate(ciphertext):
            shifted = ord(char) - ord(self.keyword[i % self.keylen]) + ord('A')
            if shifted < ord('A'):
                shifted += 26
            plaintext += chr(shifted)
        return plaintext.lower()

if __name__ == "__main__":
    keyword = "deceptive"
    cipher = VigenereCipher(keyword)

    plaintext = "wearediscoveredsaveyourself"
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
