matrix = [list(map(int, line.split(','))) for line in open('matrix.txt', 'r')]
dp = [[sum(matrix[0][0:i]) for i in range(1, 81)]] + [[sum([matrix[j][0] for j in range(i + 1)])] + [0] * 79 for i in range(1, 80)]
for r in range(1, 80):
    for c in range(1, 80):
        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + matrix[r][c]
print(dp[79][79])
