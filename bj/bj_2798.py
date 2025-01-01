N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_card_sum = 0
for a in range(0, N - 2):
    for b in range(a + 1, N -1):
        for c in range(b + 1, N):
            card_sum = cards[a] + cards[b] + cards[c]
            if card_sum > max_card_sum and card_sum <= M:
                max_card_sum = card_sum

print(max_card_sum)
