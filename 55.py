cnt = 0
for n in range(1, 10000):
    for i in range(49):
        n = int(str(n)) + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            break
    else:
        cnt += 1
print(cnt)
