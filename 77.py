from functools import cache


@cache
def count_sums(n, prev):
    global primes
    if n == 0:
        return 1
    ans = 0
    for i in range(prev, len(primes)):
        if primes[i] > n:
            break
        ans += count_sums(n - primes[i], i)
    return ans


is_prime, primes = [False] * 2 + [True] * 100, []
for n in range(2, 102):
    if is_prime[n]:
        primes.append(n)
        for j in range(n * n, 102, n):
            is_prime[j] = False
    if count_sums(n, 0) > 5000:
        print(n)
        break
