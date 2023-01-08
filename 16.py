n, ans = str(2 ** 1000), 0
for digit in n:
    ans += ord(digit) - ord('0')
print(ans)
