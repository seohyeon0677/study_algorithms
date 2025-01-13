def VPS(ps):
    stack = []
    for p in ps:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if stack:
                stack.pop()
            else:
                return "NO"
    return "YES" if not stack else "NO"

T = int(input())

for _ in range(T):
    ps = input()
    print(VPS(ps))
