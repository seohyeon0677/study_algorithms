N, M = map(int, input().split())

mon2num = {}
num2mon = {}
for i in range(1, N + 1):
    monster = input().strip()
    mon2num[monster] = i
    num2mon[i] = monster
 
for _ in range(M):
    query = input().strip()
    if query.isdigit():
        print(num2mon[int(query)])
    else:
        print(mon2num[query])
