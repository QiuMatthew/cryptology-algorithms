from src.classical_ciphers.caesar_cipher import encrypt, decrypt

def main():
    text = "hello world"
    key = 3

    encrypted_text = encrypt(text, key)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted: {decrypted_text}")

if __name__ == "__main__":
    main()
