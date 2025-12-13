from math import factorial

cnt = 0
for n in range(1, 101):
    for r in range(n + 1):
        cnt += factorial(n) // (factorial(r) * factorial(n - r)) > 1000000
print(cnt)
