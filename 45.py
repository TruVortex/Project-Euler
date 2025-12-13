i, pentagonal, hexagonal = 286, {n * (3 * n - 1) // 2 for n in range(1, 100001)}, {n * (2 * n - 1) for n in range(1, 100001)}
while i * (i + 1) // 2 not in pentagonal or i * (i + 1) // 2 not in hexagonal:
    i += 1
print(i * (i + 1) // 2)
