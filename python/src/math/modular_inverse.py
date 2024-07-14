def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find the gcd of a and b
    as well as the coefficients x and y for the equation:
    a*x + b*y = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, c):
    """
    Finds the modular inverse of a modulo c, if it exists.
    """
    gcd, x, _ = extended_gcd(a, c)
    if gcd != 1:
        # Modular inverse doesn't exist if a and c are not coprime
        raise ValueError("Modular inverse does not exist")
    else:
        return x % c
