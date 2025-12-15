from math import gcd

sols = [0] * 1500001
for m in range(1, 1500001):
    for n in range(m % 2 + 1, m, 2):
        if (l := 2 * m ** 2 + 2 * m * n) > 1500000:
            break
        if gcd(m, n) == 1:
            for k in range(1, 1500000 // l + 1):
                sols[k * l] += 1
print(sum(sol == 1 for sol in sols))
