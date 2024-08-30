
class RC4Cipher:
    def __init__(self, key: bytes) -> None:
        self.key = key
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

    def encrypt(self, plaintext: bytes) -> bytes:
        self.S = self.key_scheduling_algorithm()
        key_stream = self.pseudo_random_generation_algorithm()
        return bytes([p ^ next(key_stream) for p in plaintext])

    def decrypt(self, plaintext: bytes) -> bytes:
        self.S = self.key_scheduling_algorithm()
        key_stream = self.pseudo_random_generation_algorithm()
        return bytes([p ^ next(key_stream) for p in plaintext])


