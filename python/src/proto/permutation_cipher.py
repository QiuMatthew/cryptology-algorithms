from .base_cipher import BaseCipher

class PermutationCipher(BaseCipher):
    def __init__(self, key) -> None:
        super().__init__(key)
