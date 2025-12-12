ans = -1
for n in range(2, 10):
    i = 1
    while sum(len(str(i * j)) for j in range(1, n + 1)) <= 9:
        if sorted([digit for j in range(1, n + 1) for digit in str(i * j)]) == list('123456789'):
            ans = max(ans, int(''.join([str(i * j) for j in range(1, n + 1)])))
        i += 1
print(ans)
