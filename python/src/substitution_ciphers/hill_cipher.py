import numpy as np

from ..proto.substitution_cipher import SubstitutionCipher

class HillCipher(SubstitutionCipher):
    """
    Key: m * m matrix
    Encrypt: C = KP mod 26
    Decrypt: P = K^{-1}C mod 26
    """
    def __init__(self, key_matrix):
        self.key_matrix = np.array(key_matrix)
        self.mod = 26
        
        if not self.is_invertible():
            raise ValueError("Key matrix is not invertible in modulo 26.")

    def is_invertible(self):
        """
        Checks if the key matrix is invertible under modulo
        """
        det = int(np.round(np.linalg.det(self.key_matrix)))
        if det == 0 or np.gcd(det, self.mod) != 1:
            return False
        else:
            return True

    def matrix_mod_inv(self, matrix, mod):
        """
        Finds the modular inverse of a matrix under modulo
        """
        det = int(np.round(np.linalg.det(matrix)))
        det_inv = pow(det % mod, -1, mod)
        matrix_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod
        return matrix_inv

    def encrypt(self, plaintext):
        plaintext = self.preprocess_text(plaintext).lower()
        n = self.key_matrix.shape[0]
        
        # Padding plaintext to fit key matrix dimensions
        while len(plaintext) % n != 0:
            plaintext += 'X'
        
        plaintext_numbers = [ord(char) - ord('a') for char in plaintext]
        plaintext_matrix = np.array(plaintext_numbers).reshape(-1, n).T
        ciphertext_matrix = np.dot(self.key_matrix, plaintext_matrix) % self.mod
        ciphertext_numbers = ciphertext_matrix.T.flatten()
        
        ciphertext = ''.join(chr(num + ord('A')) for num in ciphertext_numbers)
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self.preprocess_text(ciphertext).upper()
        n = self.key_matrix.shape[0]
        
        ciphertext_numbers = [ord(char) - ord('A') for char in ciphertext]
        ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, n).T
        
        key_matrix_inv = self.matrix_mod_inv(self.key_matrix, self.mod)
        plaintext_matrix = np.dot(key_matrix_inv, ciphertext_matrix) % self.mod
        plaintext_numbers = plaintext_matrix.T.flatten()
        
        plaintext = ''.join(chr(int(num) + ord('a')) for num in plaintext_numbers)
        return plaintext

