from math import ceil

n, cnt = 1, 0
while ceil(10 ** ((n - 1) / n)) < 10:
    cnt += 10 - ceil(10 ** ((n - 1) / n))
    n += 1
print(cnt)
