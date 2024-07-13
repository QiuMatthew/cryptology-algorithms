#include <iostream>
#include <fstream>
#include <vector>

std::vector<std::string> readFile(std::string filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Failed to open file." << std::endl;
        return {};
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
        lines.push_back(line);
    }

    file.close();
    return lines;
}
