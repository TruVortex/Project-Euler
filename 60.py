from math import isqrt


def prime(i1, i2):
    global primes
    n = int(str(primes[i1]) + str(primes[i2]))
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


is_prime, primes = [False] * 2 + [True] * 10000, []
for i in range(2, 10002):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 10002, i):
            is_prime[j] = False
for i1 in range(len(primes)):
    for i2 in range(i1):
        if prime(i1, i2) and prime(i2, i1):
            for i3 in range(i2):
                if (prime(i1, i3) and prime(i3, i1) and
                    prime(i2, i3) and prime(i3, i2)):
                    for i4 in range(i3):
                        if (prime(i1, i4) and prime(i4, i1) and
                            prime(i2, i4) and prime(i4, i2) and
                            prime(i3, i4) and prime(i4, i3)):
                            for i5 in range(i4):
                                if (prime(i1, i5) and prime(i5, i1) and
                                        prime(i2, i5) and prime(i5, i2) and
                                        prime(i3, i5) and prime(i5, i3) and
                                        prime(i4, i5) and prime(i5, i4)):
                                    print(primes[i1] + primes[i2] + primes[i3] + primes[i4] + primes[i5])
                                    exit(0)
