d, pentagonal = float('inf'), [n * (3 * n - 1) // 2 for n in range(1, 5001)]
pentagonal_s = set(pentagonal)
for a in range(5000):
    for b in range(a):
        if pentagonal[a] + pentagonal[b] in pentagonal_s and pentagonal[a] - pentagonal[b] in pentagonal_s:
            d = min(d, pentagonal[a] - pentagonal[b])
print(d)
