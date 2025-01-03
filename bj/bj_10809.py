S = input().strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = []
for char in alphabet:
    answer.append(S.find(char))

print(' '.join(map(str, answer)))
