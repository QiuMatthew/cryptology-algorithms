from src.classical_ciphers.caesar_cipher import CaesarCipher

def main():
    text = "hello world"
    key = 3

    cipher = CaesarCipher(key)
    
    encrypted_text = cipher.encrypt(text)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = cipher.decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")

if __name__ == "__main__":
    main()
