n = int(input())
nums = [int(input()) for _ in range(n)]

answer = []
stack = []
current = 1
possible = True

for num in nums:
    while current <= num:
        stack.append(current)
        answer.append("+")
        current += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        possible = False
        break

if possible:
    for a in answer:
        print(a)
else:
    print("NO")
