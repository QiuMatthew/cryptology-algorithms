class ColumnarTranspositionCipher:
    def __init__(self, keyword):
        self.keyword = keyword
        self.row_count = 0

    def preprocess_text(self, text):
        # add padding
        return text + "x" * (self.row_count * len(self.keyword) - len(text))

    def encrypt(self, plaintext):
        self.row_count = (len(plaintext) - 1) // len(self.keyword) + 1
        plaintext = self.preprocess_text(plaintext)

        # Fill in the table
        table = [[plaintext[len(self.keyword) * row + col] for col in range(len(self.keyword))] for row in range(self.row_count)]
        
        sorted_indices = sorted(range(len(self.keyword)), key=lambda x: self.keyword[x])
        ciphertext = ""
        for col_index in sorted_indices:
            for row in table:
                ciphertext += row[col_index]

        return ciphertext

    def decrypt(self, ciphertext):
        self.row_count = (len(ciphertext) - 1) // len(self.keyword) + 1
        
        sorted_indices = sorted(range(len(self.keyword)), key=lambda x: self.keyword[x])
        table = [["\0" for _ in range(len(self.keyword))] for _ in range(self.row_count)]

        # Fill in the table
        i = 0
        for col_index in sorted_indices:
            for row_index in range(self.row_count):
                table[row_index][col_index] = ciphertext[i]
                i += 1
            
        plaintext = ""
        for row in table:
            for col_index in range(len(self.keyword)):
                plaintext += row[col_index]

        return plaintext

if __name__ == "__main__":
    keyword = "dcabefg"
    cipher = ColumnarTranspositionCipher(keyword)
        
    plaintext = "attackpostponeduntiltwoam"
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
