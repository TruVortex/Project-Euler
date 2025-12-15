from math import gcd

cnt = -2
for b in range(1, 12001):
    for a in range((b + 2) // 3, b // 2 + 1):
        cnt += gcd(a, b) == 1
print(cnt)
