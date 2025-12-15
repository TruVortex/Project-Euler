ans, prime_divisors = 0, [[] for i in range(1000001)]
for i in range(2, 1000001):
    if not prime_divisors[i]:
        for j in range(i, 1000001, i):
            prime_divisors[j].append(i)
    totient = i
    for prime in prime_divisors[i]:
        totient *= (prime - 1)
        totient //= prime
    ans += totient
print(ans)
