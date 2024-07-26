from math import sqrt, ceil
class MatrixTranspositionCipher:
    def __init__(self):
        self.matrix_size = 0

    def preprocess_text(self, text):
        return text + "x" * (int(pow(self.matrix_size, 2)) - len(text))

    def encrypt(self, plaintext):
        self.matrix_size = ceil(sqrt(len(plaintext)))
        plaintext = self.preprocess_text(plaintext)
        matrix = [[plaintext[row_index * self.matrix_size + col_index] for col_index in range(self.matrix_size)] for row_index in range(self.matrix_size)]

        ciphertext = ""
        for col_index in range(self.matrix_size):
            for row_index in range(self.matrix_size):
                ciphertext += matrix[row_index][col_index]
        return ciphertext

    def decrypt(self, ciphertext):
        self.matrix_size = int(sqrt(len(ciphertext)))
        matrix = [[ciphertext[row_index * self.matrix_size + col_index] for col_index in range(self.matrix_size)] for row_index in range(self.matrix_size)]

        plaintext = ""
        for col_index in range(self.matrix_size):
            for row_index in range(self.matrix_size):
                plaintext += matrix[row_index][col_index]
        return plaintext

if __name__ == "__main__":
    cipher = MatrixTranspositionCipher()

    plaintext = "canyouunderstand"
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
