import itertools

ans, primes = 0, (2, 3, 5, 7, 11, 13, 17)
for n in itertools.permutations(map(str, range(10))):
    if all(int(''.join(n)[i + 1:i + 4]) % primes[i] == 0 for i in range(7)):
        ans += int(''.join(n))
print(ans)
