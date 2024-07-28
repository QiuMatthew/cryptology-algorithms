from .base_cipher import BaseCipher

class SubstitutionCipher(BaseCipher):
    def __init__(self, key) -> None:
        super().__init__(key)

    def preprocess_text(self, text):
        """
        Remove spaces, numbers, commas, periods and other non-alphabetic symbols
        Convert uppercase letters to lowercase
        """
        processed_text = ""
        for char in text:
            if char.isalpha():
                processed_text += char
        
        return processed_text

