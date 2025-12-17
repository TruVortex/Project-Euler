matrix = [list(map(int, line.split(','))) for line in open('input', 'r')]
dp = [[matrix[i][0]] + [float('inf')] * 79 for i in range(80)]
for c in range(1, 80):
    for i in range(80):
        for r in range(80):
            if r == 0:
                dp[r][c] = min(dp[r + 1][c], dp[r][c - 1]) + matrix[r][c]
            elif r == 79:
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + matrix[r][c]
            else:
                dp[r][c] = min(dp[r - 1][c], dp[r + 1][c], dp[r][c - 1]) + matrix[r][c]
print(min(dp[i][79] for i in range(80)))
