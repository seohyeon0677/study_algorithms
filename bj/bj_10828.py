N = int(input())
todo = [list(input().split()) for _ in range(N)]

stack = []
for do in todo:
    if do[0] == "push":
        stack.append(int(do[1]))
    elif do[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif do[0] == "size":
        print(len(stack))
    elif do[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif do[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
