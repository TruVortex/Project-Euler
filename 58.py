from math import isqrt


def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


n, cnt = 3, 3
while 10 * cnt >= 2 * n - 1:
    n += 2
    cnt += prime(n ** 2 - (dn := (n ** 2 - (n - 2) ** 2) // 4)) + prime(n ** 2 - 2 * dn) + prime(n ** 2 - 3 * dn)
print(n)
