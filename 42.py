cnt = 0
for word in open('words.txt', 'r').read().replace('"', '').split(','):
    value, n = sum(ord(ch) - ord('A') + 1 for ch in word), 1
    while value > n * (n + 1) // 2:
        n += 1
    if value == n * (n + 1) // 2:
        cnt += 1
print(cnt)
