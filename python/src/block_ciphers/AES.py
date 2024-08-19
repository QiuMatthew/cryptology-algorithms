from ..proto.block_cipher import BlockCipher

class AESCipher(BlockCipher):
    RCON = [
        0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36
    ]
    S_BOX = [
        [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
    ]

    def __init__(self, key) -> None:
        self.key = [ord(c) for c in key]
        self.round_key_matrices = self.expand_keys()

    def expand_keys(self) -> list[list[list[int]]]:
        """
        Generate round keys that will be used in each round.
        For AES-128, we have a 128-bit encryption key.
        We put the encryption key into a 4 * 4 byte matrix, like what we do for plaintext.
        The matrix have four columns w[0] to w[3], each column is called a word,
        and we will create and append more column one by one, until we have w[0] to w[43].
        w[0] to w[3] is the encryption key, w[4] to w[7] is the first round key, and so on.
        """
        w = [[0] * 4] * 44
        # Copy the encryption key into the first 4 words (columns) of w
        for i in range(4):
            w[i] = [self.key[4 * i], self.key[4 * i + 1], self.key[4 * i + 2], self.key[4 * i + 3]]

        # Generate remaining words
        for i in range(4, 44):
            if i % 4 != 0:
                w[i] = self._xor_words(w[i - 4], w[i - 1])
            else:
                # left rotation
                temp = [0] * 4
                temp[0], temp[1], temp[2], temp[3] = w[i - 1][1], w[i - 1][2], w[i - 1][3], w[i - 1][0]
                # byte substitution
                temp = [self.S_BOX[byte >> 4][byte & 0x0F] for byte in temp]
                # exclusive or with round constant
                temp[0] ^= self.RCON[i // 4 - 1]
                w[i] = self._xor_words(w[i - 4], temp)
        # print(f"round_keys: {w}")

        # Split into separated round key matrices
        round_key_matrices = [[[w[round * 4 + col][row] for col in range(4)] for row in range(4)] for round in range(11)]
        return round_key_matrices

    def add_round_key(self, state: list[list[int]], round: int) -> list[list[int]]:
        for row in range(4):
            for col in range(4):
                state[row][col] ^= self.round_key_matrices[round][row][col]
        return state

    def substitute_bytes(self, state: list[list[int]]) -> list[list[int]]:
        for row in range(4):
            for col in range(4):
                state[row][col] = self.S_BOX[state[row][col] >> 4][state[row][col] & 0x0F]
        return state

    def shift_rows(self, state: list[list[int]]) -> list[list[int]]:
        state[1][0], state[1][1], state[1][2], state[1][3] = state[1][1], state[1][2], state[1][3], state[1][0]
        state[2][0], state[2][1], state[2][2], state[2][3] = state[2][2], state[2][3], state[2][0], state[2][1]
        state[3][0], state[3][1], state[3][2], state[3][3] = state[3][3], state[3][0], state[3][1], state[3][2]
        return state

    def galois_field_mul(self, a, b):
        """
        This is the multiplication defined on GF(2^8)
        The modulo is 0x11b, which corresponds to the irreducible polynomial x^8 + x^4 + x^3 + x + 1
        """
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p % 256

    def mix_columns(self, state: list[list[int]]) -> list[list[int]]:
        for col in range(4):
            a = [state[row][col] for row in range(4)]
            state[0][col] = self.galois_field_mul(a[0], 2) ^ self.galois_field_mul(a[1], 3) ^ a[2] ^ a[3]
            state[1][col] = a[0] ^ self.galois_field_mul(a[1], 2) ^ self.galois_field_mul(a[2], 3) ^ a[3]
            state[2][col] = a[0] ^ a[1] ^ self.galois_field_mul(a[2], 2) ^ self.galois_field_mul(a[3], 3)
            state[3][col] = self.galois_field_mul(a[0], 3) ^ a[1] ^ a[2] ^ self.galois_field_mul(a[3], 2)
        return state

    def matrix_to_matrix_encrypt(self, state: list[list[int]]) -> list[list[int]]:
        # Add encryption key
        state = self.add_round_key(state, 0)
        # print(f"Initial key added: {state}")
        # Nine rounds of process
        for round in range(1, 10):
            state = self.substitute_bytes(state)
            # print(f"SubBytes finished: {state}")
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, round)
        # print(f"9 rounds ended: {state}")
        # Last round, without mix column
        state = self.substitute_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, 10)
        return state

    def encrypt(self, plaintext: str) -> str:
        assert len(plaintext) == 16, "Plaintext must be 16 bytes long."
        plaintext_bytes = [ord(c) for c in plaintext]
        # print(f"plaintext_bytes: {plaintext_bytes}")
        plaintext_matrix = self._bytes_to_matrix(plaintext_bytes)
        # print(f"plaintext_matrix: {plaintext_matrix}")
        ciphertext_matrix = self.matrix_to_matrix_encrypt(plaintext_matrix)
        # print(f"ciphertext_matrix: {ciphertext_matrix}")
        ciphertext_bytes = self._matrix_to_bytes(ciphertext_matrix)
        # print(f"ciphertext_bytes: {ciphertext_bytes}")
        ciphertext_hex = self._bytes_to_hex(ciphertext_bytes)
        # print(f"ciphertext_hex = {ciphertext_hex}")
        return ciphertext_hex

    def decrypt(self, ciphertext: str) -> str:
        return super().decrypt(ciphertext)

    def _xor_words(self, word1: list[int], word2: list[int]):
        """
        This function takes bitwise exclusive or of two words, each word is composed of 4 bytes
        """
        xor_word = [0] * 4
        for i in range(4):
            xor_word[i] = word1[i] ^ word2[i]

        return xor_word

    def _bytes_to_matrix(self, byte_list: list[int]) -> list[list[int]]:
        """
        In AES-128, the matrix is always 4 * 4 for plaintext, ciphertext and keys.
        The bytes are aligned to fill columns first and then rows.
        For instance:
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
        will be aligned as
        1  5  9  13
        2  6  10 14
        3  7  11 15
        4  8  12 16
        and
        matrix[0][3] = 13 as it is the element in the first row and fourth (last) column
        """
        matrix = [[byte_list[col * 4 + row] for col in range(4)] for row in range(4)]
        return matrix

    def _matrix_to_bytes(self, state: list[list[int]]) -> list[int]:
        """
        The inverse of _bytes_to_matrix, used to decode state matrix
        """
        byte_list = [state[row][col] for col in range(4) for row in range(4)]
        return byte_list

    def _bytes_to_hex(self, byte_list) -> str:
        return ''.join(f'{byte:02x}' for byte in byte_list)

if __name__ == "__main__":
    key = "thisisakey123456"
    cipher = AESCipher(key)
    plaintext = "thisisplaintext1"
    
    ciphertext_hex = cipher.encrypt(plaintext)
    print(ciphertext_hex)
