# Computes the prime factors of a given number
# Returns the factors in a list
# Input: a positive integer

import math


def factors(n):
    assert isinstance(n, int)
    factor = []
    if n < 2:
        return [n]
    while n % 2 == 0:
        factor.append(2)
        n = n / 2
    for i in range(3, int(math.ceil(math.sqrt(n))) + 1, 2):
        while n % i == 0 and n > i:
            factor.append(i)
            n = n / i
        if i > n:
            break
    if n > 2:
        factor.append(n)
    return factor

