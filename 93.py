import itertools


def find_pos(nums):
    if len(nums) == 1:
        return {abs(nums[0])}
    pos = set()
    for i, j in itertools.combinations(range(len(nums)), 2):
        nnums = [nums[k] for k in range(len(nums)) if k != i and k != j]
        pos |= find_pos(nnums + [nums[i] + nums[j]])
        pos |= find_pos(nnums + [nums[i] * nums[j]])
        pos |= find_pos(nnums + [nums[i] - nums[j]])
        if nums[j]:
            pos |= find_pos(nnums + [nums[i] / nums[j]])
        if nums[i]:
            pos |= find_pos(nnums + [nums[j] / nums[i]])
    return pos


ans = (None, -1)
for comb in itertools.combinations(range(1, 10), 4):
    pos, n = find_pos(comb), 1
    while n in pos:
        n += 1
    if n > ans[1]:
        ans = (comb, n)
print(''.join(map(str, ans[0])))
