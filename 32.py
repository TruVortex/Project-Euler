from math import isqrt

total = 0
for n in range(1, 100000):
    for divisor in range(1, isqrt(n) + 1):
        if n % divisor == 0 and sorted(list(str(n)) + list(str(divisor)) + list(str(n // divisor))) == list('123456789'):
            total += n
            break
print(total)
