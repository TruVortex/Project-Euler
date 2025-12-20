ans, roman_to_int = 0, {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for line in open('input', 'r'):
    acc, subtract = 0, 'M'
    for ch in line.strip():
        if roman_to_int[ch] > roman_to_int[subtract]:
            acc -= 2 * roman_to_int[subtract]
        acc += roman_to_int[ch]
        subtract = ch
    shortest = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')[acc % 10]
    acc //= 10
    shortest = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')[acc % 10] + shortest
    acc //= 10
    shortest = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')[acc % 10] + shortest
    ans += len(line.strip()) - acc // 10 - len(shortest)
print(ans)
