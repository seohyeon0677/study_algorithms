# X가 승리할 수 있으면 1, 아니면 0

# xx.xx
# xxxx.
# .xxxx

def play(game):
    # 가로
    for i in range(10):
        for j in range(6):
            if  game[i][j] == 'X' and game[i][j+1] == 'X' and game[i][j+2] == 'X' and game[i][j+3] == 'X' and game[i][j+4] == '.':
                return 1
            if  game[i][j] == '.' and game[i][j+1] == 'X' and game[i][j+2] == 'X' and game[i][j+3] == 'X' and game[i][j+4] == 'X':
                return 1
            if  game[i][j] == 'X' and game[i][j+1] == 'X' and game[i][j+2] == '.' and game[i][j+3] == 'X' and game[i][j+4] == 'X':
                return 1
    
    # 세로
    for i in range(6):
        for j in range(10):
            if game[i][j] == 'X' and game[i+1][j] == 'X' and game[i+2][j] == 'X' and game[i+3][j] == 'X' and game[i+4][j] == '.':
                return 1
            if game[i][j] == '.' and game[i+1][j] == 'X' and game[i+2][j] == 'X' and game[i+3][j] == 'X' and game[i+4][j] == 'X':
                return 1
            if game[i][j] == 'X' and game[i+1][j] == 'X' and game[i+2][j] == '.' and game[i+3][j] == 'X' and game[i+4][j] == 'X':
                return 1

    # 우하향 대각선
    for i in range(6):
        for j in range(6):
            if game[i][j] == 'X' and game[i+1][j+1] == 'X' and game[i+2][j+2] == 'X' and game[i+3][j+3] == 'X' and game[i+4][j+4] == '.':
                return 1
            if game[i][j] == '.' and game[i+1][j+1] == 'X' and game[i+2][j+2] == 'X' and game[i+3][j+3] == 'X' and game[i+4][j+4] == 'X':
                return 1
            if game[i][j] == 'X' and game[i+1][j+1] == 'X' and game[i+2][j+2] == '.' and game[i+3][j+3] == 'X' and game[i+4][j+4] == 'X':
                return 1

    # 좌하향 대각선선
    for i in range(5, 10):
        for j in range(5, 10):
            if game[i][j] == 'X' and game[i-1][j-1] == 'X' and game[i-2][j-2] == 'X' and game[i-3][j-3] == 'X' and game[i-4][j-4] == '.':
                return 1
            if game[i][j] == '.' and game[i-1][j-1] == 'X' and game[i-2][j-2] == 'X' and game[i-3][j-3] == 'X' and game[i-4][j-4] == 'X':
                return 1
            if game[i][j] == 'X' and game[i-1][j-1] == 'X' and game[i-2][j-2] == '.' and game[i-3][j-3] == 'X' and game[i-4][j-4] == 'X':
                return 1
    
    return 0

game = [input().strip() for _ in range(10)]
print(play(game))
