import itertools
from math import isqrt


def prime(n):
    if n == 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


ans = -1
for l in range(1, 8):
    for n in itertools.permutations(map(str, range(1, l + 1))):
        if prime(int(''.join(n))):
            ans = max(ans, int(''.join(n)))
print(ans)
