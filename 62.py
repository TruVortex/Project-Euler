from collections import defaultdict

n, cnt = 1, defaultdict(int)
while cnt[(freq := tuple(str(n ** 3).count(i) for i in '1234567890'))] < 4:
    cnt[freq] += 1
    n += 1
print(min(pos ** 3 for pos in range(n) if tuple(str(pos ** 3).count(i) for i in '1234567890') == freq))
