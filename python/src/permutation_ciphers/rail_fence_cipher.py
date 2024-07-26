class RailFenceCipher:
    def __init__(self, row_count):
        self.row_count = row_count

    def encrypt(self, plaintext):
        # corner case
        if self.row_count == 1:
            return plaintext

        # for n row and m column, we have (m - 1)(n - 1) + 1 <= len(plaintext) < m(n - 1) + 1
        self.col_count = (len(plaintext) - 1) // (self.row_count - 1)
        table = [["\0" for _ in range(self.col_count)] for _ in range(self.row_count)]

        for i, char in enumerate(plaintext):
            if i == 0:
                table[0][0] = plaintext[0]
                continue
            col_index = (i - 1) // (self.row_count - 1)
            row_offset = (i - 1) % (self.row_count - 1)
            if col_index % 2 == 0:
                row_index = row_offset + 1
            else:
                row_index = self.row_count - row_offset - 2
            table[row_index][col_index] = char

        ciphertext = ""
        for row in table:
            for char in row:
                if char != '\0':
                    ciphertext += char

        return ciphertext

    def decrypt(self, ciphertext):
        # corner case
        if self.row_count == 1:
            return ciphertext

        self.col_count = (len(ciphertext) - 1) // (self.row_count - 1)
        table = [["\0" for _ in range(self.col_count)] for _ in range(self.row_count)]
        
        table[0][0] = ciphertext[0]
        row, col, i = 0, 1, 1
        while row < self.row_count:
            # first row
            if row == 0:
                while col < self.col_count:
                    table[row][col] = ciphertext[i]
                    col += 2
                    i += 1
                col = 0
                row += 1
                # print("first row done")
            # last row
            elif row == self.row_count - 1:
                while col < self.col_count:
                    table[row][col] = ciphertext[i]
                    col += 2
                    i += 1
                    if i >= len(ciphertext):
                        break
                row += 1
                # print("last row done")
            # rows in the middle
            else:
                while col < self.col_count:
                    table[row][col] = ciphertext[i]
                    col += 1
                    i += 1
                col = 0
                row += 1
                # print(f"No.{row + 1} row done")
        
        plaintext = table[0][0]
        for col in range(self.col_count):
            for row_offset in range(self.row_count - 1):
                if col % 2 == 0:
                    plaintext += table[row_offset + 1][col]
                else:
                    plaintext += table[self.row_count - row_offset - 2][col]

        return plaintext

if __name__ == "__main__":
    row_count = 2
    cipher = RailFenceCipher(row_count)

    plaintext = "meetmeafterthetogaparty"
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")

