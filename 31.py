dp = [1] + [0] * 200
for coin in (1, 2, 5, 10, 20, 50, 100, 200):
    for i in range(coin, 201):
        dp[i] += dp[i - coin]
print(dp[200])
