n, ans = 1, 0
for i in range(1, 101):
    n *= i
for digit in str(n):
    ans += ord(digit) - ord('0')
print(ans)
