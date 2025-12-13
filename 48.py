acc = 0
for i in range(1, 1001):
    acc += pow(i, i, 10 ** 10)
    acc %= 10 ** 10
print(acc)
