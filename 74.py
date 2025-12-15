from math import factorial

cnt, memoize = 0, list(factorial(i) for i in range(10))
for n in range(1, 1000000):
    loop = 2
    while n not in (169, 3901, 1454, 871, 45361, 872, 45362) and loop <= 60:
        n = sum(memoize[int(digit)] for digit in str(n))
        loop += 1
    cnt += (loop + (n in (169, 3901, 1454))) == 60
print(cnt)
