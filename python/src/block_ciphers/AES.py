from ..proto.block_cipher import BlockCipher

class AESCipher(BlockCipher):
    RCON = [
        0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36
    ]

    def __init__(self, key) -> None:
        self.key = key

    def expand_keys(self):
        """
        Generate round keys that will be used in each round.
        For AES-128, we have a 128-bit encryption key.
        We put the encryption key into a 4 * 4 byte matrix, like what we do for plaintext.
        The matrix have four columns w[0] to w[3], each column is called a word,
        and we will create and append more column one by one, until we have w[0] to w[43].
        w[0] to w[3] is the encryption key, w[4] to w[7] is the first round key, and so on.
        """
        w = [[0] * 4] * 44
        print(w)

        # Copy the original key into the first 4 words (columns) of w
        for i in range(4):
            w[i] = [self.key[4 * i], self.key[4 * i + 1], self.key[4 * i + 2], self.key[4 * i + 3]]

        # TODO: Generate remaining words

        return w
    def encrypt(self, plaintext: str) -> str:
        return super().encrypt(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return super().decrypt(ciphertext)


if __name__ == "__main__":
    key = "thisisakey123456"
    cipher = AESCipher(key)
    cipher.expand_keys()
