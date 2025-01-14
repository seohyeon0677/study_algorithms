N = int(input())
cards = list(map(int, input().split()))
M = int(input())
Q = list(map(int, input().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for q in Q:
    print(count.get(q, 0))
