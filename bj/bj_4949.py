def balance(tc):
    open = '(['
    close = ')]'

    stack = []
    for s in tc:
        if s in open:
            stack.append(s)
        elif s in close:
            if not stack or open.index(stack.pop()) != close.index(s):
                return False
    return not stack


TC = []
while True:
    str = input()
    if str == ".":
        break
    else:
        TC.append(str)

for tc in TC:
    if balance(tc):
        print("yes")
    else:
        print("no")
