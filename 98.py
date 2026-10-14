from functools import reduce
from itertools import permutations
from math import isqrt


def convert(word, mapp):
    return reduce(lambda total, ch: total * 10 + mapp[ch], word, 0)

def square(num):
    return isqrt(num) * isqrt(num) == num

words, ans = eval(f"[{open('words.txt', 'r').read()}]"), -1
for word1 in words:
    for word2 in words:
        if word1 != word2 and (letters := sorted(word1)) == sorted(word2):
            for mapping in permutations(range(1, 10), len(letters)):
                mapp = dict(zip(letters, mapping))
                num1, num2 = convert(word1, mapp), convert(word2, mapp)
                if square(num1) and square(num2):
                    ans = max(ans, num1, num2)
print(ans)
