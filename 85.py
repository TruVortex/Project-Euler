ans, rows = (-1, -1), 2
while rows * (rows - 1) // 2 <= 2000000:
    cols = 2
    while (cnt := rows * (rows - 1) * cols * (cols - 1) // 4) <= 2100000:
        if abs(cnt - 2000000) < abs(ans[1] - 2000000):
            ans = ((rows - 1) * (cols - 1), cnt)
        cols += 1
    rows += 1
print(ans[0])
