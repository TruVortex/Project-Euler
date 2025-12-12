from math import isqrt


def prime(n):
    if n == 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


total, cnt, n = 0, 0, 11
while cnt < 11:
    if all(prime(int(str(n)[i:])) for i in range(len(str(n)))) and all(prime(int(str(n)[:i + 1])) for i in range(len(str(n)))):
        total += n
        cnt += 1
    n += 1
print(total)
