tc = input()

count = 0
stack = []
for i in range(len(tc)):
    if tc[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if tc[i - 1] == "(":
            count += len(stack)
        else:
            count += 1

print(count)
