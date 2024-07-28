from ..proto.substitution_cipher import SubstitutionCipher

class VigenereCipher(SubstitutionCipher):
    """
    Key: key = k_0 k_1 k_2 ... k_{n-1}
    Encrypt: c_i = p_i + k_i mod 26
    Decrypt: p_i = c_i - k_i mod 26
    """
    def __init__(self, keyword) -> None:
        self.keyword = keyword.upper()
        self.keylength = len(self.keyword)

    def preprocess_text(self, text):
        text = text.replace(" ", "")
        for char in text:
            if not char.isalpha():
                raise ValueError("text must be alphabetic only")
        return text

    def encrypt(self, plaintext):
        plaintext = self.preprocess_text(plaintext)
        ciphertext = ""
        for i, char in enumerate(plaintext):
            if char.isalpha():
                shifted = ord(char) + ord(self.keyword[i % self.keylength]) - ord('A')
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
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                shifted = ord(char) - ord(self.keyword[i % self.keylength]) + ord('A')
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

if __name__ == "__main__":
    keyword = "deceptive"
    cipher = VigenereCipher(keyword)

    plaintext = "wearediscoveredsaveyourself"
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
