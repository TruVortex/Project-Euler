a = b = 1
for i in range(3, 5000):
    a, b = b, a + b
    if len(str(b)) >= 1000:
        print(i)
        break
