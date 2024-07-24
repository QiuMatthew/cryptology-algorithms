class PlayfairCipher:
    def __init__(self, keyword):
        self.keyword = keyword
        self.key_square = self.generate_key_square(keyword)
    
    def generate_key_square(self, keyword):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_square = ""
        for char in keyword.upper():
            if char not in key_square and char in alphabet:
                key_square += char
        for char in alphabet:
            if char not in key_square:
                key_square += char
        return [list(key_square[i:i+5]) for i in range(0, 25, 5)]
    
    def preprocess_text(self, text):
        # Use upper case only
        text = text.upper().replace("J", "I").replace(" ", "")
        processed_text = ""
        i = 0
        while i < len(text):
            processed_text += text[i]
            if i + 1 < len(text) and text[i] == text[i + 1]:
                processed_text += "X"
            elif i + 1 < len(text):
                processed_text += text[i + 1]
                i += 1
            i += 1
        if len(processed_text) % 2 != 0:
            processed_text += "X"
        return processed_text

    def find_position(self, char):
        for i, row in enumerate(self.key_square):
            for j, c in enumerate(row):
                if c == char:
                    return i, j
        raise ValueError(f"Character {char} not found in key square")

    def encrypt_pair(self, a, b):
        row_a, col_a = self.find_position(a)
        row_b, col_b = self.find_position(b)
        if row_a == row_b:
            return self.key_square[row_a][(col_a + 1) % 5] + self.key_square[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            return self.key_square[(row_a + 1) % 5][col_a] + self.key_square[(row_b + 1) % 5][col_b]
        else:
            return self.key_square[row_a][col_b] + self.key_square[row_b][col_a]

    def decrypt_pair(self, a, b):
        row_a, col_a = self.find_position(a)
        row_b, col_b = self.find_position(b)
        if row_a == row_b:
            return self.key_square[row_a][(col_a - 1) % 5] + self.key_square[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            return self.key_square[(row_a - 1) % 5][col_a] + self.key_square[(row_b - 1) % 5][col_b]
        else:
            return self.key_square[row_a][col_b] + self.key_square[row_b][col_a]

    def encrypt(self, plaintext):
        plaintext = self.preprocess_text(plaintext)
        ciphertext = ""
        for i in range(0, len(plaintext), 2):
            ciphertext += self.encrypt_pair(plaintext[i], plaintext[i + 1])
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            plaintext += self.decrypt_pair(ciphertext[i], ciphertext[i + 1])
        return plaintext

if __name__ == "__main__":
    cipher = PlayfairCipher("MONARCHY")
    encrypted = cipher.encrypt("HELLO WORLD")
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
