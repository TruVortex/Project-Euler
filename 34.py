total, fact = 0, (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
for n in range(10, fact[9] * 7 + 1):
    if n == sum(fact[int(c)] for c in str(n)):
        total += n
print(total)
