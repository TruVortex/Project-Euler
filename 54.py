from statistics import mode, multimode


def find_strength(hand):
    values, suits = sorted(int(card.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')[:-1]) for card in hand), {card[1] for card in hand}
    return [values[::-1],
            (len(set(values)) == 4, mode(values)),
            (len(set(values)) == 3 and all(values.count(i) < 3 for i in range(1, 15)), *sorted(multimode(values), reverse=True)),
            (len(set(values)) == 3 and any(values.count(i) == 3 for i in range(1, 15)), mode(values)),
            (any(values == list(range(i, i + 5)) for i in range(1, 10)), values[0]),
            (len(suits) == 1, values[-1]),
            (len(set(values)) == 2 and any(values.count(i) == 3 for i in range(1, 15)), mode(values)),
            (any(values.count(i) == 4 for i in range(1, 15)), mode(values)),
            (any(values == list(range(i, i + 5)) for i in range(1, 10)) and len(suits) == 1, values[0])]

cnt = 0
for line in open('poker.txt', 'r'):
    prev = cnt
    player1, player2 = find_strength(line[:14].split()), find_strength(line[15:].split())
    if (r1 := max(i if rank[0] else -1 for i, rank in enumerate(player1))) == (r2 := max(i if rank[0] else -1 for i, rank in enumerate(player2))):
        if r1 == 0:
            cnt += player1[0] > player2[0]
        elif r1 == 2:
            cnt += (player1[2][1] > player2[2][1] or player1[2][1] == player2[2][1] and
                   (player1[2][2] > player2[2][2] or player1[2][1] == player2[2][1] and player1[0] > player2[0]))
        else:
            cnt += player1[r1][1] > player2[r1][1] or player1[r1][1] == player2[r1][1] and player1[0] > player2[0]
    else:
        cnt += r1 > r2
print(cnt)
