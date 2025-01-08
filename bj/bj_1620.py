N, M = map(int, input().split())
have = [input().strip() for _ in range(N)]

def find_monster(monster):
    if monster.isdigit():
        return have[int(monster) - 1]
    else:
        return have.index(monster) + 1
    
for _ in range(M):
    print(find_monster(input().strip()))
