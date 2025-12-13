n = 1
while len({tuple(sorted(str(i * n))) for i in range(1, 7)}) != 1:
    n += 1
print(n)
