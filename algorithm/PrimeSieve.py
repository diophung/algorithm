# Problem: find all prime numbers up to an integer N, N >= 2
import math


def prime_sieve(n):
    print('\r\nAll primes up to [' + str(n) + ']: ')
    is_prime = [True] * (n + 1)
    sqrt_n = math.ceil(math.sqrt(n))

    for i in range(2, int(sqrt_n)):
        if is_prime[i] is True:
            k = 0
            num = i * i + k * i
            while num <= n:
                is_prime[num] = False
                k += 1
                num = i * i + (k * i)
    for index, num in enumerate(is_prime):
        if is_prime[index] is True and index >= 2:
            print(index)
    print('\r\n')


prime_sieve(2)
prime_sieve(19)
prime_sieve(30)
