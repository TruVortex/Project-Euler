import itertools
from math import isqrt


def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


for a in range(1000, 10000):
    if prime(a):
        for b in itertools.permutations(list(str(a))):
            if a < (b := int(''.join(b))) < (10000 + a) / 2 and prime(b) and prime(2 * b - a) and tuple(str(2 * b - a)) in set(itertools.permutations(list(str(a)))):
                print(str(a) + str(b) + str(2 * b - a))
