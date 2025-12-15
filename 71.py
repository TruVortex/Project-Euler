from math import gcd

numer, denom = 0, 1
while denom + 7 <= 1000000:
    numer, denom = numer + 3, denom + 7
    numer, denom = numer // gcd(numer, denom), denom // gcd(numer, denom)
print(numer, denom)
