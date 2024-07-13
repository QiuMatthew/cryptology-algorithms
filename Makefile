# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11 -Wall -Iinclude

# Directories
SRC_DIR = src
INCLUDE_DIR = include
OBJ_DIR = obj
BIN_DIR = bin
TEST_DIR = tests

# Source directories
BLOCK_CIPHERS_DIR = $(SRC_DIR)/block_ciphers
CLASSICAL_CIPHERS_DIR = $(SRC_DIR)/classical_ciphers
HASH_FUNCTIONS_DIR = $(SRC_DIR)/hash_functions
MAC_DIR = $(SRC_DIR)/message_authentication_code
PUBLIC_KEY_DIR = $(SRC_DIR)/public_key_cryptography
QUANTUM_CRYPTO_DIR = $(SRC_DIR)/quantum_cryptography
STREAM_CIPHER_DIR = $(SRC_DIR)/stream_ciphers
UTILS_DIR = $(SRC_DIR)/utils

# Test directories
TEST_BLOCK_CIPHERS_DIR = $(TEST_DIR)/test_block_ciphers
TEST_CLASSICAL_CIPHERS_DIR = $(TEST_DIR)/test_classical_ciphers
TEST_HASH_FUNCTIONS_DIR = $(TEST_DIR)/test_hash_functions
TEST_MAC_DIR = $(TEST_DIR)/test_message_authentication_code
TEST_PUBLIC_KEY_DIR = $(TEST_DIR)/test_public_key_cryptography
TEST_QUANTUM_CRYPTO_DIR = $(TEST_DIR)/test_quantum_cryptography
TEST_STREAM_CIPHERS_DIR = $(TEST_DIR)/test_stream_ciphers
TEST_UTILS_DIR = $(TEST_DIR)/test_utils

# Target executable
TARGET = $(BIN_DIR)/cryptology_algorithms

# Source files
SRCS = $(wildcard $(BLOCK_CIPHERS_DIR)/*.cpp) \
       $(wildcard $(CLASSICAL_CIPHERS_DIR)/*.cpp) \
       $(wildcard $(HASH_FUNCTIONS_DIR)/*.cpp) \
       $(wildcard $(MAC_DIR)/*.cpp) \
       $(wildcard $(PUBLIC_KEY_DIR)/*.cpp) \
       $(wildcard $(QUANTUM_CRYPTO_DIR)/*.cpp) \
       $(wildcard $(STREAM_CIPHER_DIR)/*.cpp) \
       $(wildcard $(UTILS_DIR)/*.cpp) \
       $(SRC_DIR)/main.cpp
OBJS = $(SRCS:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

# Test files
TEST_SRCS = $(wildcard $(TEST_BLOCK_CIPHERS_DIR)/*.cpp) \
            $(wildcard $(TEST_CLASSICAL_CIPHERS_DIR)/*.cpp) \
            $(wildcard $(TEST_HASH_FUNCTIONS_DIR)/*.cpp) \
            $(wildcard $(TEST_MAC_DIR)/*.cpp) \
            $(wildcard $(TEST_PUBLIC_KEY_DIR)/*.cpp) \
            $(wildcard $(TEST_QUANTUM_CRYPTO_DIR)/*.cpp) \
            $(wildcard $(TEST_STREAM_CIPHERS_DIR)/*.cpp) \
            $(wildcard $(TEST_UTILS_DIR)/*.cpp)
TEST_OBJS = $(TEST_SRCS:$(TEST_DIR)/%.cpp=$(OBJ_DIR)/%.o)

# Create necessary directories
$(shell mkdir -p $(OBJ_DIR) $(BIN_DIR) $(OBJ_DIR)/block_ciphers $(OBJ_DIR)/classical_ciphers $(OBJ_DIR)/hash_functions $(OBJ_DIR)/message_authentication_code $(OBJ_DIR)/public_key_cryptography $(OBJ_DIR)/quantum_cryptography $(OBJ_DIR)/stream_ciphers $(OBJ_DIR)/utils $(OBJ_DIR)/test_block_ciphers $(OBJ_DIR)/test_classical_ciphers $(OBJ_DIR)/test_hash_functions $(OBJ_DIR)/test_message_authentication_code $(OBJ_DIR)/test_public_key_cryptography $(OBJ_DIR)/test_quantum_cryptography $(OBJ_DIR)/test_stream_ciphers $(OBJ_DIR)/test_utils)

# Default target
all: $(TARGET)

# Link object files to create the executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile source files to object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Compile test files to object files
$(OBJ_DIR)/%.o: $(TEST_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Test target
test: $(TEST_OBJS)
	$(CXX) $(CXXFLAGS) -o $(BIN_DIR)/test $^
	$(BIN_DIR)/test

# Clean target
clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

# Phony targets
.PHONY: all clean test
