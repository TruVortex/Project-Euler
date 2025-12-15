ans, prime_divisors = (-1, float('inf')), [[] for i in range(10000000)]
for i in range(2, 10000000):
    if not prime_divisors[i]:
        for j in range(i, 10000000, i):
            prime_divisors[j].append(i)
    totient = i
    for prime in prime_divisors[i]:
        totient *= (prime - 1)
        totient //= prime
    if sorted(str(totient)) == sorted(str(i)) and i / totient < ans[1]:
        ans = (i, i / totient)
print(ans[0])
