from math import isqrt


def prime(n):
    if n == 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


n = 9
while True:
    if not prime(n):
        for i in range(1, isqrt(n // 2) + 1):
            if prime(n - 2 * i * i):
                break
        else:
            break
    n += 2
print(n)
