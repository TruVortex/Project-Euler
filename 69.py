ans, primes_factors = (-1, -1), [[] for i in range(1000001)]
for i in range(2, 1000001):
    if not primes_factors[i]:
        for j in range(i, 1000001, i):
            primes_factors[j].append(i)
    cur = 1
    for prime in primes_factors[i]:
        cur *= prime / (prime - 1)
    if cur > ans[1]:
        ans = (i, cur)
print(ans[0])
