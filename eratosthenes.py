# Sieve of Eratosthenes
# An algorithm for finding all prime numbers smaller or equal to n


def eratosthenes(n):
    assert isinstance(n, int)
    if n < 2:
        return set()
    else:
        primes = set()
        for i in range(2, n + 1):
            primes.add(i)
        p = 2
        while p < n:
            x = 2
            while x * p <= n:
                primes.discard(x * p)
                x = x + 1
            p = p + 1
            if primes.__contains__(p):
                continue
            else:
                while (not primes.__contains__(p)) and p < n:
                    p = p + 1

        return primes

