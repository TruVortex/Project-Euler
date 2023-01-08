dp = {}


def collatz(x):
    global dp
    if x == 1:
        return 1
    elif x in dp:
        return dp[x]
    elif x % 2:
        dp[x] = 1 + collatz(3 * x + 1)
        return dp[x]
    dp[x] = 1 + collatz(x // 2)
    return dp[x]


ans = [collatz(i) for i in range(1, 1000001)]
print(ans.index(max(ans)) + 1)
