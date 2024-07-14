#pragma once
#include <string>

class Caesar {
public:
    std::string encrypt(const std::string &plaintext, const std::string &key);
    std::string decrypt(const std::string &ciphertext, const std::string &key);
};
