def encrypt(plaintext, key):
    # Ensure the key is an integer
    key = int(key)
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                ciphertext += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    # Ensure the key is an integer
    key = int(key)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                plaintext += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                plaintext += chr(shifted)
        else:
            plaintext += char
    return plaintext
