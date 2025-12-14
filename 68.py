import itertools


def get_ring(outer, inner):
    return ''.join([str(outer[i]) + str(inner[i]) + str(inner[i - 4]) for i in range(5)])


ans = ''
for outer in itertools.combinations(range(1, 11), 5):
    outer = sorted(outer)
    for clockwise in itertools.permutations(outer[1:]):
        for in1 in set(range(1, 11)) - set(outer):
            for in2 in set(range(1, 11)) - set(outer) - {in1}:
                inner = [in1, in2, -1, -1, (desired_sum := outer[0] + in1 + in2) - in1 - clockwise[3]]
                inner[3] = desired_sum - inner[4] - clockwise[2]
                inner[2] = desired_sum - inner[3] - clockwise[1]
                if inner[1] + inner[2] + clockwise[0] == desired_sum and set(inner) | set(outer) == set(range(1, 11)):
                    ans = max(ans, get_ring(outer[:1] + list(clockwise), inner))
print(ans)
