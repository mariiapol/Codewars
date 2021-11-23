def generate_primes(n):
    # Sieve of Eratosthenes algorithm

    i = 2
    is_prime = [True if x>1 else False for x in range(n + 1)]
    while i * i <= n:
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
        i += 1
    return [x for x in range(n+1) if is_prime[x]]


class Primes:
    n = 20000000
    prime_numbers = generate_primes(n)

    @staticmethod
    def stream():
        yield from Primes.prime_numbers
