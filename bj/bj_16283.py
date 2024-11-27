# a : 양 1마리 사료
# b : 염소 1마리 사료
# n : 전체 몇마리
# w : 전체 소비 사료

a, b, n, w = map(int, input().split())

# lamb + goat = n
# lamb * a + goat * b = w

answer = []
for lamb in range(1, n):
    goat = n - lamb
    if lamb * a + goat * b == w:
        answer.append((lamb, goat))

if len(answer) != 1:
    print("-1")
else:
    lamb, goat = answer[0]
    print(lamb, goat)
