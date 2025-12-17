from collections import defaultdict

ans, vertices_in, pos_nums = '', defaultdict(set), set()
for line in open('keylog.txt', 'r'):
    vertices_in[line[1]].add(line[0])
    vertices_in[line[2]] |= set(line[:2])
    pos_nums |= set(line[:3])
while pos_nums:
    to_remove_node = None
    for key in pos_nums:
        if not vertices_in[key]:
            to_remove_node = key
            ans += str(key)
    pos_nums.remove(to_remove_node)
    for value in vertices_in.values():
        if to_remove_node in value:
            value.remove(to_remove_node)
print(ans)
