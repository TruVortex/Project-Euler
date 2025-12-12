total = 1
for i in range(3, 1002, 2):
    total += 4 * i * i - 6 * (i * i - (i - 2) * (i - 2)) // 4
print(total)
