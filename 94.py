from math import isqrt, gcd

total = 0
for m in range(2, isqrt(1000000000)):
    for n in range(m % 2 + 1, m, 2):
        if gcd(m, n) == 1:
            a, b, c = m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2
            if c + c + (base := 2 * min(a, b)) > 1000000000:
                break
            elif base in (c - 1, c + 1):
                total += c + c + base
print(total)
