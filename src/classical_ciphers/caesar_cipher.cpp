#include "../../include/classical_ciphers/caesar_cipher.h"
#include <string>

std::string Caesar::encrypt(const std::string &plaintext, const std::string &key) {
    // TODO: input validation
    
    std::string ciphertext;
    int keyInt = std::stoi(key);
    for (char c : plaintext) {
        ciphertext.push_back('a' + (c - 'a' + keyInt) % 26);
    }
    return ciphertext;
}

std::string Caesar::decrypt(const std::string &ciphertext, const std::string &key) {
    // TODO: input validation
    
    std::string plaintext;
    int keyInt = -std::stoi(key);
    while (keyInt < 0) {
        keyInt += 26;
    }
    for (char c : ciphertext) {
        plaintext.push_back('a' + (c - 'a' + keyInt) % 26);
    }
    return plaintext;
}

