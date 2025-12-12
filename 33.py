from math import gcd

numer = denom = 1
for a in range(10, 100):
    for b in range(a + 1, 100):
        if (a % 10 or b % 10) and a % 11 and b % 11:
            digits_a, digits_b = set(list(str(a))), set(list(str(b)))
            if (digits_a & digits_b != set() and digits_a != digits_b and
                    a * int((digits_b - digits_a).pop()) == b * int((digits_a - digits_b).pop())):
                numer *= a
                denom *= b
print(denom // gcd(numer, denom))
