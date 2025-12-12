from math import isqrt


def prime(n):
    if n == 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


cnt = 0
for n in range(1, 1000000):
    if all(prime(int(str(n)[i:] + str(n)[:i])) for i in range(len(str(n)))):
        cnt += 1
print(cnt)
