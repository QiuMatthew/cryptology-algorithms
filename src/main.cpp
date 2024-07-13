#include <iostream>
#include "../include/utils/sample_util.h"
#include "../include/utils/read_file.h"

int main() {
    std::cout << "Hello, World!" << std::endl;

    // Test a function from the utils directory
    sample_util_function();
    readFile("src/main.cpp");

    return 0;
}

