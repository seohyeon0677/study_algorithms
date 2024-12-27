# X가 승리할 수 있으면 1, 아니면 0

def play(board, r, c):
    directions = [
        (0,1),
        (1,0),
        (1,1),
        (1,-1)
    ]

    for dr, dc in directions:
        count = 1

        for i in range(1,5):
            nr, nc = r + dr * i, c + dc * i
            if 0 <= nr < 10 and 0 <= nc < 10 and board[nr][nc] == 'X':
                count += 1
            else:
                break

        for i in range(1,5):
            nr, nc = r - dr * i, c - dc * i
            if 0 <= nr < 10 and 0 <= nc < 10 and board[nr][nc] == 'X':
                count += 1
            else:
                break

        if count >= 5:
            return True
    return False

def win(board):
    for r in range(10):
        for c in range(10):
            if board[r][c] == '.':
                board[r] = board[r][:c] + 'X' + board[r][c+1:]
                if play(board, r, c):
                    return 1
                board[r] = board[r][:c] + '.' + board[r][c+1:]
    return 0

board = [input().strip() for _ in range(10)]
print(win(board))
