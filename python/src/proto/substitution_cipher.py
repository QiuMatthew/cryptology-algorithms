from .base_cipher import BaseCipher

class SubstitutionCipher(BaseCipher):
    '''
    We use lowercase letters for plaintext and uppercase letters for ciphertext
    '''
    def preprocess_plaintext(self, text) -> str:
        '''
        Remove spaces, numbers and other non-alphabetic symbols
        Convert uppercase letters to lowercase
        '''
        return "".join(char.lower() for char in text if char.isalpha())

    def preprocess_ciphertext(self, text) -> str:
        '''
        Remove spaces, numbers and other non-alphabetic symbols
        Convert lowercase letters to uppercase
        '''
        return "".join(char.upper() for char in text if char.isalpha())
