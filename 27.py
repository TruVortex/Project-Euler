from math import isqrt


def prime(n):
    if -1 <= n <= 1:
        return False
    for i in range(2, isqrt(abs(n)) + 1):
        if n % i == 0:
            return False
    return True


ans = (-1, -1)
for b in range(-1000, 1001):
    if prime(b):
        for a in range(-1000, 1001):
            n = 0
            while prime(n * n + a * n + b):
                n += 1
            if n > ans[1]:
                ans = (a * b, n - 1)
print(ans[0])
