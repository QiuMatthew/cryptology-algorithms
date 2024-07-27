from abc import ABC, abstractmethod

class BaseCipher(ABC):
    def __init__(self, key) -> None:
        self.key = key

    @abstractmethod
    def encrypt(self, plaintext) -> str:
        pass

    @abstractmethod
    def decrypt(self, ciphertext) -> str:
        pass

