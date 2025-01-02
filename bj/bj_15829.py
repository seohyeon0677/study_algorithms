L = int(input())
alpha = input()

r = 31
M = 1234567891

H = 0
for i in range(len(alpha)):
    n = ord(alpha[i]) - ord('a') + 1
    H += n * (r ** i)

print(H % M)
