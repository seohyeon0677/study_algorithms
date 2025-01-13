N = int(input())
words = list(input() for _ in range(N))

good_words = 0
for word in words:
    
    stack = []
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    
    if not stack:
        good_words += 1

print(good_words)
