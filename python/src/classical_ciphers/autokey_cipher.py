class AutokeyCipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()

    def preprocess_text(self, text):
        text = text.replace(" ", "")
        for char in text:
            if not char.isalpha():
                raise ValueError("text must be alphabetic only")
        text = text.upper()
        return text

    def encrypt(self, plaintext):
        plaintext = self.preprocess_text(plaintext)
        ciphertext = ""
        for i, char in enumerate(plaintext):
            if i < len(self.keyword):
                ciphertext += chr(ord(char) + ord(self.keyword[i]) - ord("A"))
            else:
                ciphertext += chr(ord(char) + ord(plaintext[i - len(self.keyword)]) - ord("A"))
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i, char in enumerate(ciphertext):
            if i < len(self.keyword):
                shifted = ord(char) - ord(self.keyword[i]) + ord('A')
                if shifted < ord('A'):
                    shifted += 26
            else:
                shifted = ord(char) - ord(plaintext[i - len(self.keyword)]) + ord('A')
                if shifted < ord('A'):
                    shifted += 26
            plaintext += char(shifted)
        return plaintext

if __name__ == "__main__":
    keyword = "deceptive"
    cipher = AutokeyCipher(keyword)
    
    plaintext = "wearediscoveredsaveyourself"
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")

