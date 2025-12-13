ans, is_prime, primes = (-1, -1), [False] * 2 + [True] * 1000000, []
for i in range(2, 1000002):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 1000002, i):
            is_prime[j] = False
for i in range(1, len(primes)):
    primes[i] += primes[i - 1]
for i in range(len(primes)):
    for j in range(i - ans[1]):
        if primes[i] - primes[j] < 1000000 and is_prime[primes[i] - primes[j]] and i - j + 1 > ans[1]:
            ans = (primes[i] - primes[j], i - j + 1)
print(ans[0])
