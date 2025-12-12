total = 0
for n in range(10, 6 * (9 ** 5) + 1):
    if n == sum(int(c) ** 5 for c in str(n)):
        total += n
print(total)
