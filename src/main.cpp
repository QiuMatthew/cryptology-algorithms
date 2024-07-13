#include <iostream>
#include <ostream>
#include "../include/utils/sample_util.h"
#include "../include/utils/read_file.h"
#include "../include/classical_ciphers/caesar_cipher.h"

int main() {
    std::cout << "Hello, World!" << std::endl;

    // Test a function from the utils directory
    sample_util_function();
    readFile("src/main.cpp");

    // Caesar Cipher
    Caesar caesarCipher;
    std::string plaintext = "hello";
    std::string key = "3";
    std::string ciphertext = caesarCipher.encrypt(plaintext, key);
    std::string decrypted = caesarCipher.decrypt(ciphertext, key);

    std::cout << "======Caesar Cipher======" << std::endl;
    std::cout << "plaintext = " << plaintext << std::endl;
    std::cout << "key = " << key << std::endl;
    std::cout << "ciphertext = " << ciphertext << std::endl;
    std::cout << "decrypted = " << decrypted << std::endl;

    return 0;
}

