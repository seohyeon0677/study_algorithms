M = int(input())

S = set()
for i in range(M):
    command = input().split()
    do = command[0]
    x = int(command[1]) if len(command) > 1 else None
    
    if do == 'add':
        S.add(x)
    if do == 'remove':
        S.discard(x)
    if do == 'check':
        print(1 if x in S else 0)
    if do == 'toggle':
        S.remove(x) if x in S else S.add(x)
    if do == 'all':
        S = set(range(1, 21))
    if do == 'empty':
        S = set()
