is_prime, primes = [False] * 2 + [True] * 1000000, []
for i in range(2, 1000002):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 1000002, i):
            is_prime[j] = False
for p in primes:
    if any(sum(not (str(p)[0] == i and j == 0) and is_prime[int(str(p).replace(str(i), str(j)))] for j in range(10)) >= 8 for i in str(p)):
        print(p)
        break
