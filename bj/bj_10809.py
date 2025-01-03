def counts(S, a):
    for i in range(len(S)):
        if S[i] == a:
            return i
    return -1

S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = []
for char in alphabet:
    answer.append(counts(S, char))

print(' '.join(map(str, answer)))
