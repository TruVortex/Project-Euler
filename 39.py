ans = (-1, -1)
for p in range(1, 1001):
    cnt = 1
    for a in range(1, p):
        for b in range(a, p - a + 1):
            if a ** 2 + b ** 2 == (p - a - b) ** 2:
                cnt += 1
    if cnt >= ans[1]:
        ans = (p, cnt)
print(ans[0])
