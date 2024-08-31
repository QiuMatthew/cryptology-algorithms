class RC4Cipher:
    def __init__(self, key: str) -> None:
        self.key = key.encode()
        self.S = self.key_scheduling_algorithm()

    def key_scheduling_algorithm(self) -> list[int]:
        # Initialize S as identity permutaion
        S = list(range(256))
        # Use key to permute S
        j = 0
        key_length = len(self.key)
        for i in range(256):
            j = (j + S[i] + self.key[i % key_length]) % 256
            # Swap
            S[i], S[j] = S[j], S[i]
        return S

    def pseudo_random_generation_algorithm(self):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            # Swap
            self.S[i], self.S[j] = self.S[j], self.S[i]  
            K = self.S[(self.S[i] + self.S[j]) % 256]
            yield K

    def encrypt(self, plaintext: str) -> str:
        """
        The RC4 encryption
        Input: plaintext string
        Output: ciphertext hex, since the encrypted byte might not be decodable to valid character
        """
        plaintext_bytes = plaintext.encode()
        self.S = self.key_scheduling_algorithm()
        key_stream = self.pseudo_random_generation_algorithm()
        ciphertext_bytes = bytes([p ^ next(key_stream) for p in plaintext_bytes])
        return ciphertext_bytes.hex()

    def decrypt(self, ciphertext: str) -> str:
        """
        The RC4 decryption
        Input: ciphertext hex
        Output: plaintext string
        """
        ciphertext_bytes = bytes.fromhex(ciphertext)
        self.S = self.key_scheduling_algorithm()
        key_stream = self.pseudo_random_generation_algorithm()
        plaintext_bytes =  bytes([p ^ next(key_stream) for p in ciphertext_bytes])
        plaintext = plaintext_bytes.decode()
        return plaintext


