import struct
import math

# Initialize the MD5 state (A, B, C, D)
A = 0x67452301
B = 0xefcdab89
C = 0x98badcfe
D = 0x10325476

# Auxiliary functions, take 32-bit inputs and produce 32-bit output
def F(x, y, z):
    return (x & y) | (~x & z)

def G(x, y, z):
    return (x & z) | (y & ~z)

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | ~z)

K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

# Shift amounts S
S = [
    7, 12, 17, 22,  # Round 1
    5, 9, 14, 20,   # Round 2
    4, 11, 16, 23,  # Round 3
    6, 10, 15, 21   # Round 4
] * 4  # Repeat each set 4 times

def pad_message(message_bytes: bytes) -> bytes:
    message_bit_len = len(message_bytes) * 8
    # remind that the final 64 bits are reserved for original length
    padding_bit_len = 512 - (message_bit_len + 64) % 512
    padding = b''
    if padding_bit_len > 0:
        padding = b'\x80' + b'\x00' * int(padding_bit_len / 8 - 1)
    padded_message_bytes = message_bytes + padding + struct.pack('<Q', message_bit_len)
    return padded_message_bytes

def process_chunk(chunk, state):
    a, b, c, d = state

    # Break chunk into sixteen 32-bit words
    M = list(struct.unpack('<16I', chunk))

    # Perform the 64 operations
    for i in range(64):
        if 0 <= i <= 15:
            f = F(b, c, d)
            g = i
        elif 16 <= i <= 31:
            f = G(b, c, d)
            g = (5 * i + 1) % 16
        elif 32 <= i <= 47:
            f = H(b, c, d)
            g = (3 * i + 5) % 16
        elif 48 <= i <= 63:
            f = I(b, c, d)
            g = (7 * i) % 16

        temp = d
        d = c
        c = b
        b = (b + ((a + f + K[i] + M[g]) & 0xFFFFFFFF << S[i]) & 0xFFFFFFFF | (a + f + K[i] + M[g]) & 0xFFFFFFFF >> (32 - S[i])) & 0xFFFFFFFF
        a = temp

    # Add this chunk's hash to result so far
    return [(state[i] + val) & 0xFFFFFFFF for i, val in enumerate([a, b, c, d])]

def md5_finalize(state):
    return struct.pack('<4I', *state)

def md5(message):
    state = [A, B, C, D]

    padded_message = pad_message(message)
    for i in range(0, len(padded_message), 64):
        chunk = padded_message[i:i+64]
        state = process_chunk(chunk, state)

    return md5_finalize(state).hex()
    
def str_to_bytes(message_string: str) -> bytes:
    return message_string.encode()

def bytes_to_str(message_bytes: bytes) -> str:
    return message_bytes.decode()

result = md5(b"hello world")
print(result)  # Should output: 5eb63bbbe01eeed093cb22bb8f5acdc3

