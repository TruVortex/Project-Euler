def count_factors(n):
    global primes
    return sum(n % prime == 0 for prime in primes)


n, is_prime, primes = 1, [False] * 2 + [True] * 2000, []
for i in range(2, 2002):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 2002, i):
            is_prime[j] = False
while {count_factors(n), count_factors(n + 1), count_factors(n + 2), count_factors(n + 3)} != {4}:
    n += 1
print(n)
