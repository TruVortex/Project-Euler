from math import isqrt, sqrt

print(sum(sum(map(int, str(isqrt(n * 10 ** 198)))) for n in range(1, 101) if sqrt(n) % 1))
