from math import sqrt

m, acc = 0, 0
while acc <= 1000000:
    m += 1
    cnt = 0
    for b in range(1, m + 1):
        for c in range(1, b + 1):
            if sqrt(m ** 2 + (b + c) ** 2) % 1 == 0:
                cnt += 1
    acc += cnt
print(m)
