from .base_cipher import BaseCipher

class SubstitutionCipher(BaseCipher):
    def __init__(self, key) -> None:
        super().__init__(key)

